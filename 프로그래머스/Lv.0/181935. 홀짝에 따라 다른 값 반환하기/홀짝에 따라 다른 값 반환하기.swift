import Foundation

func solution(_ n:Int) -> Int {
    var result : Int = 0
    if n % 2 == 0 {
        for num in 1...n{
            if num % 2 == 0 {
                result += (num * num)
            }
        }
    }else {
        for num in 1...n{
            if num % 2 == 1 {
                result += num
            }
        }
    }
    return result
}