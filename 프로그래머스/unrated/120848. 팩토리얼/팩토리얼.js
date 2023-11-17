function solution(m) {
    let answer = 0
    for (let n = 1; n < 11; n++){
        let fac = 1
        for (let num = 1; num < n+1; num++){
            fac *= (num)
        }
        if (fac <= m) {
            answer = n
        }else{
            break
        }
    }
    return answer;
}