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
            ZStack{
                Color("customdark")
                
                scro()
                    }.tabItem {
                        Image(systemName: "house")
                        Text("home")
            }
            
            Text("2")
                .tabItem {
                    Image(systemName: "flame.fill")
                    Text("flame")
                }
        }.preferredColorScheme(.dark)
    }
}

struct scro : View{
    var lineargradientcolor = LinearGradient(gradient: Gradient(colors: [Color.purple,Color.pink,Color.white]), startPoint: .top, endPoint: .bottom)
    
    var body: some View{
        ScrollView{
            VStack{
                ForEach(0..<100){ item in
                    HStack(alignment:.center){
                        Circle()
                            .opacity(0)
                            .background(lineargradientcolor)
                            .frame(width: 50, height: 50)
                            .clipShape(Circle())
                        Text("content\(item)")
                    }
                }
            }
        }.edgesIgnoringSafeArea(.all)
            .padding()
            .frame(width:500)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
