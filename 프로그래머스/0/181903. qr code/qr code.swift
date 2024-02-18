import Foundation

func solution(_ q:Int, _ r:Int, _ code:String) -> String {
    let leng = code.count
    let strArr = Array(code)
    var arr : [Character] = []
    var n = 0
    var i = (q * n) + r

    while i < leng {
        arr.append(strArr[i])
        n += 1
        i = (q * n) + r
    }
    
    return String(arr)
}