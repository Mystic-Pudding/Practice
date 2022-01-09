//
//  ContentView.swift
//  API_Tutorial
//
//  Created by mystic on 2021/05/30.
//

import SwiftUI

struct ContentView: View {
    @State var data = test(name: "first", old: "0")
    @State var search_url = "http://127.0.0.1:5000/"
    @State var chageable = "false"
    
    func getData(){
        let urlString = search_url
        let url = URL(string: urlString)
        
        URLSession.shared.dataTask(with: url!){data,_, error in
            DispatchQueue.main.async {
                if let data = data{
                    do {
                        let decoder = JSONDecoder()
                        let decodeData = try decoder.decode(test.self, from: data)
                        self.data = decodeData
                    } catch {
                        print("error")
                    }
                }
            }
            
        }.resume()
    }
    
    var body: some View {
        VStack{
            Button("start") {
                search_url="http://127.0.0.1:5000/"
                self.getData()
                
            }
            Button("Change") {
                search_url="http://127.0.0.1:5000/?name=hello&old=15"
                self.getData()
                chageable = "true"
            }
        }
        VStack{
            Text("\(data.name)")
            Text("\(data.old)")
            Text("\(self.search_url)")
            Text("\(self.chageable)")
        }
    }
}

