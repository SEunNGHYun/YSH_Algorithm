import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var stk : [Int] = []
    var i = 0
    var last : Int! = 0
    while i < arr.count {
        if stk.count == 0 {
            stk.append(arr[i])
            i = i+1
        }else {
            last = stk.popLast()
            if last < arr[i] {
                stk.append(last)
                stk.append(arr[i])
                i = i + 1
            }
        }
    }
    return stk
}