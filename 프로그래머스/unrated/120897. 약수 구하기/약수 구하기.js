function solution(n) {
    var answer = []
    let m = Math.floor(Math.sqrt(n))
    for (let num = 1; num <= m; num ++){
        if (n % num == 0){
            answer.push(num)
            if ((n / num) !== (n / (n/num))){
                answer.push((n / num))
            }
        }
    }
    return answer.sort((a,b) => a-b)
}