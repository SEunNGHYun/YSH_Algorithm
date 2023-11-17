function solution(n) {
    var answer = 0
    function check (num) {
        let um = Math.floor(Math.pow(num, 0.5))
        let count = 0
        for (let m = 1; m <= um; m++){
            if (num % m == 0) ++count
            if (count >= 2) return true
        }
        return false
    }
    
    for (let num = 4; num <= n; num++) {
        if(check(num))  answer += 1       
    }
    return answer
}