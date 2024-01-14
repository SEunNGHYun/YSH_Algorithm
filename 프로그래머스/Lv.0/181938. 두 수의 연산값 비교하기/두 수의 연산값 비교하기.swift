import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let strInt = Int(String(a) + String(b))!
    let num = a * b * 2
    
    return num > strInt ? num : strInt
}