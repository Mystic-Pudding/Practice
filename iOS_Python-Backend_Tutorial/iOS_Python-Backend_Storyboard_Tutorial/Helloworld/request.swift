
import Foundation

struct test : Decodable {
    var name : String
    var old : String
    enum CodingKeys: String, CodingKey{
        case name = "name"
        case old = "old"
    }
}
