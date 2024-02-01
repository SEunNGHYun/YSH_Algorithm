import Foundation

func solution(_ n:Int) -> [Int] {
    var num :Int = n
    var result : [Int] = []
    while num > 1 {       
        result.append(num)
        if (num % 2 == 0) {
            num = num / 2
        }else {
            num = num * 3 + 1
        }
    }
    result.append(num)

    return result
}