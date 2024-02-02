import Foundation

func solution(_ number:String) -> Int {
    var sum = 0
    for s in number {
        sum += Int(String(s))!
    }
    
    return sum % 9
}