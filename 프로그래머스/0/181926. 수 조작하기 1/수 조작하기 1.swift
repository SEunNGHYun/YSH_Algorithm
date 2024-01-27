import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    let controls : [Character] = Array(control)
    var result = n
    
    for c in controls {
        if (c == "w") {
            result += 1
        }else if (c == "a") {
            result -= 10
        }else if (c == "s") {
            result -= 1
        }else if (c == "d") {
            result += 10
        }
    }
    return result
}