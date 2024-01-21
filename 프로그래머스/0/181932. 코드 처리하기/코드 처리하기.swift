import Foundation

func solution(_ code:String) -> String {
    let s = Array(code.map{String($0)})
    var ret : [String] = []
    var mode = false // == 0 true == 1
    
    for i in 0...(code.count-1) {
        if s[i] == "1" {
            mode = !mode
            continue
        }
        if mode && (i % 2 == 1) {
            ret.append(s[i])
        }
        else if !mode && (i % 2 == 0) {
            ret.append(s[i])
        }
    }
    
    
    return ret.isEmpty ? "EMPTY" : ret.joined() 
}