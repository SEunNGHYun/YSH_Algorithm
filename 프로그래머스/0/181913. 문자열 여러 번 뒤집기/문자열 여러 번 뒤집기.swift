import Foundation

func solution(_ my_string:String, _ queries:[[Int]]) -> String {
    var strArr = Array(my_string)
    for query in queries {
        strArr[query[0]...query[1]].reverse()
    }
    return String(strArr)
}