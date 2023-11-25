function solution(quiz) {
    function check (q) {
        let math_q = q.split(' ')
        if (math_q[1] == '-') {
            if (Number(math_q[0]) - Number(math_q[2]) == math_q[4]){
                return 'O'
            }else{
                return 'X'
            }
        }else if (math_q[1] == '+') {
             if (Number(math_q[0]) + Number(math_q[2]) == math_q[4]){
                return 'O'
            }else{
                return 'X'
            }
        }
    }
    return quiz.map(q => check(q))
}