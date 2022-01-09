//
//  request.swift
//  API_Tutorial
//
//  Created by mystic on 2021/05/30.
//

import Foundation

struct test : Decodable {
    var name : String
    var old : String
    enum CodingKeys: String, CodingKey{
        case name = "name"
        case old = "old"
    }
}
