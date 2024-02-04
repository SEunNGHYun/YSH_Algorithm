import Foundation

func solution(_ my_string:String) -> [String] {
    var result : [String] = []
    var arr = Array(my_string)
    for i in 0..<arr.count {
        var str = arr[i..<arr.count]
        result.append(String(str))
    }
    
    return result.sorted(by:<)
}