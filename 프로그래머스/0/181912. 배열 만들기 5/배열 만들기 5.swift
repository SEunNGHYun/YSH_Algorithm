import Foundation

func solution(_ intStrs:[String], _ k:Int, _ s:Int, _ l:Int) -> [Int] {
    var result:[Int] = []
    for nums in intStrs {
        var num = Array(nums)[s...(s+l - 1)]
        let n = Int(String(num))!
        if n > k {
            result.append(n)
        }
    }
    return result
}