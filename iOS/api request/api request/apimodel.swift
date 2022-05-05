//
//  apimodel.swift
//  api request
//
//  Created by mystic on 2022/05/05.
//

import Foundation

// MARK: - Results
struct Results: Decodable {
    let articles: [numbers]
}

// MARK: - Article
struct numbers: Decodable, Hashable{
    let greeting : String
}
