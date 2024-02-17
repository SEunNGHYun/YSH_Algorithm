import Foundation

func solution(_ my_string:String, _ is_prefix:String) -> Int {
    var prefixArr :[String] = []
    var result = 0
    let strArr = Array(my_string)
    for i in 1...(strArr.count-1) {
        prefixArr.append(String(strArr[...i]))
    }
    
    for pre in prefixArr {
        if pre == is_prefix {
            result = 1
        }
    }
    return result
}