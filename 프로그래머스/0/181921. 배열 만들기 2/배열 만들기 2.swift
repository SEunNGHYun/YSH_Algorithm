import Foundation

func solution(_ l:Int, _ r:Int) -> [Int] {
    var result : [Int] = []
    
    for num in l...r {
        var check = true
        for s in String(num) {
            if s == "5" || s == "0" {
                continue
            }else {
                check = false
                break
            }
        }
        
        if check {
            result.append(num)
        }
    }
    
    return result.count > 0 ? result : [-1]
}