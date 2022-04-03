//
//  ContentView.swift
//  tabv
//
//  Created by mystic on 2022/04/03.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView{
            scro()
                .tabItem {
                    Image(systemName: "house")
                    Text("home")
                }
            Text("2")
                .tabItem {
                    Image(systemName: "flame.fill")
                    Text("flame")
                }
        }
    }
}

struct scro : View{
    var body: some View{
        ScrollView{
            VStack{
                ForEach(0..<100){ item in
                    Text("\(item)")
                        .font(.largeTitle)
                }
            }
        }.frame(width: 300, height: .infinity)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .preferredColorScheme(.dark)
    }
}
