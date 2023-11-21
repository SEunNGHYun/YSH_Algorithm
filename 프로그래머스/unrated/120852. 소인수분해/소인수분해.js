function solution(n) {
    var answer = [];
    var num = 2
    while (num <= n) {
        if (n % num == 0){
            n = Math.floor(n / num)
            if (answer.indexOf(num) == -1){
                answer.push(num)
            }
        }else {
            num += 1
        }
    }
    return answer;
}