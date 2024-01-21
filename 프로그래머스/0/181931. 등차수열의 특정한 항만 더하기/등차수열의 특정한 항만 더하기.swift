import Foundation

func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var result = 0
    for (idx, val) in included.enumerated() {
        if included[idx] {
            result += (idx * d) + a
        }
    }
    return result 
}