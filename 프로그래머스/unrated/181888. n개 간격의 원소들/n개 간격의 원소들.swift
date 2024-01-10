import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var result : [Int] = []
    for i in 0..<num_list.count {
        if i % n == 0 {
            result.append(num_list[i])
        }
    }
    return result
}