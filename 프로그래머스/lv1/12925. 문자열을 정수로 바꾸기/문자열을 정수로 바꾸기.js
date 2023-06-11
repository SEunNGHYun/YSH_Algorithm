function solution(s) {
    let num = 0
    if (s[0] == '+' || s[0] == '-'){ 
        num = Number(s.slice(1))
        if (s[0] == '-') {
            num = 0 - num
        }
    } else{
        num = Number(s)
    }
    return num
}