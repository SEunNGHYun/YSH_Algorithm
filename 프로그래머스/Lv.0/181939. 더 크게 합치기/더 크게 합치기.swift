import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let strInt1 = Int(String(a) + String(b))!
    let strInt2 = Int(String(b) + String(a))!
    return strInt1 > strInt2 ? strInt1 : strInt2
}