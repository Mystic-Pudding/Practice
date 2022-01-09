
import Foundation

struct test : Decodable {
    var name : [String]
    var old : String
    var length : Int
    enum CodingKeys: String, CodingKey{
        case name = "name"
        case old = "old"
        case length = "length"
    }
}
