import Foundation

func solution(_ num_list:[Int]) -> Int {
    var o = "", e = ""
    for num in num_list {
        if (num % 2 == 1) {o += String(num)} 
        else if (num % 2 == 0) {e += String(num)} 
    }
    
    return Int(o)! + Int(e)!
}