import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    let arr = Array(my_string)

    return String(arr[...(n-1)])
}