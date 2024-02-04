import Foundation

func solution(_ my_string:String, _ is_suffix:String) -> Int {
    var s = Array(my_string)
    var result = 0
    var sArr :[String] = []
    for i in 0..<s.count {
        sArr.append(String(s[i...]))
    }
    for ss in sArr {
        if ss == is_suffix {
            result = 1
            break
        }
    }
    return result
}