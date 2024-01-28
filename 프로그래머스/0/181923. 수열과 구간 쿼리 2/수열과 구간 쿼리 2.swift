import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var result : [Int] = []
    var arr2 = arr
    for q in queries {
        var num = -1
        var s = arr2[q[0]...q[1]].sorted()
        for ss in s {
            if q[2] < ss {
                num = ss
                break
            }
        }
        result.append(num)
    }
    return result
}