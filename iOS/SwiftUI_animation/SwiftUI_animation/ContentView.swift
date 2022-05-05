//
//  ContentView.swift
//  SwiftUI_animation
//
//  Created by mystic on 2022/03/30.
//

import SwiftUI

struct ContentView: View {
    @State var blur : Bool = false
    @State var reduction : Bool = false
    var body: some View {
        Image("imagesample")
            .blur(radius: blur ? 5 : 0)
            .scaleEffect(reduction ? 0.7 : 1)
            .onTapGesture {
                withAnimation(.easeInOut) {
                    self.blur.toggle()
                    self.reduction.toggle()
                }
            }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

