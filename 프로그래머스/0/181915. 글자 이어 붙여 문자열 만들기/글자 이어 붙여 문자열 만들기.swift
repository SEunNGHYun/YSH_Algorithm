import Foundation

func solution(_ my_string:String, _ index_list:[Int]) -> String {
    var arr = Array(my_string)
    var result = ""
    for i in index_list {
        result += String(arr[i])
    }
    return result
}