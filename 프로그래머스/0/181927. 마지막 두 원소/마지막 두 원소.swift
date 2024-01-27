import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var nums :[Int] = num_list
    let last : Int = num_list.count - 1
    var val : Int 
    if (num_list[last] > num_list[last-1]) {
        val = num_list[last] - num_list[last - 1]
    }else{
        val = num_list[last] * 2
    }
    nums.append(val)
    return nums
}