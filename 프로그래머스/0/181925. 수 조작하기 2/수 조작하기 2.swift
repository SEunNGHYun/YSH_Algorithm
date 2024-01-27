import Foundation

func solution(_ numLog:[Int]) -> String {
    var pre = numLog[0]
    var next = numLog[1]
    var result = ""
    for i in 2..<numLog.count {
        if ((next - pre) == 1) {
            result += "w"
        }else if ((next - pre) == -1) {
            result += "s"
        }else if ((next - pre) == -10) {
            result += "a"
        }else if ((next - pre) == 10) {
            result += "d"
        }
        pre = next
        next = numLog[i]
    }
    print(pre, next)
    if ((next - pre) == 1) {
            result += "w"
        }else if ((next - pre) == -1) {
            result += "s"
        }else if ((next - pre) == -10) {
            result += "a"
        }else if ((next - pre) == 10) {
            result += "d"
        }
    
    return result
}