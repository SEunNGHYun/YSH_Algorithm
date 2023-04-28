function solution(s)
{
    var arr = []
    
    for (let i = 0; i < s.length; i++){
        if(arr.length > 0){
            var last = arr.pop() 
            if(last != s[i]){
                arr.push(last)
                arr.push(s[i])
            }
        }else{
            arr.push(s[i])
        }
    }
    if(arr.length > 0){
        return 0
    }else{
        return 1
    }
}