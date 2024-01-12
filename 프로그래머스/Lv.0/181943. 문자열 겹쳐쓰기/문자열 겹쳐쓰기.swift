import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    var start : String = my_string.substring(to:s)
    let index : Int = overwrite_string.count + s
    var end : String = my_string.substring(from:index)
    return start + overwrite_string + end 
}