import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var result : String = ""
    for i in 0..<str1.count {
        let index :String.Index = str1.index(str1.startIndex, offsetBy: i)
        result += (String(str1[index]) + String(str2[index]))
    }
    return result
}