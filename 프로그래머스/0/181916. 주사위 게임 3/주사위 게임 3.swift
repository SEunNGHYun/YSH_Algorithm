import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int, _ d:Int) -> Int {
    let arr = [a,b,c,d]
    let s = Set(arr)
    var dict = [Int: Int]()

    if s.count == 1 {
        return 1111 * arr[0]
    }
    
    for n in arr {
        dict[n] = (dict[n] ?? 0) + 1
    }
    print(dict)
    if s.count == 2 {
        var n1 = 0, n2 = 0, n3: [Int] = []
        for (key, val) in dict {
            if val == 1 {
                n2 = key
            }else if val == 3 {
                n1 = key
            }else if val == 2 {
                n3.append(key)
            }
        }
        if n3.count == 2 {
            return (n3[1] + n3[0]) * abs(n3[1] - n3[0])
        }else {
            return (10 * n1 + n2) * (10 * n1 + n2) 
        }
        return 0
    }else if s.count == 3 {
        var n1 : [Int] = []
        for (key, val) in dict {
            if val == 1 {
                n1.append(key)
            }
        }
        return n1[0] * n1[1]
    }else {
        return arr.min()!
    }
}