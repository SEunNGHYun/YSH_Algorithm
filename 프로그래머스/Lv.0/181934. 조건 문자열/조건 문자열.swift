import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    if ineq == ">" {
        if eq == "!" {
           if n > m {
               return 1
           }else{
               return 0
           }
        }else {
            if n >= m {
               return 1
           }else{
               return 0
           }
        }
    }else {
        if eq == "!" {
           if n < m {
               return 1
           }else{
               return 0
           }
        }else {
           if n <= m  {
               return 1
           }else{
               return 0
           }
        }
    }
    //stride
}