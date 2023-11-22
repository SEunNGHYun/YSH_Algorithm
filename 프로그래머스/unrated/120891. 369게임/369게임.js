function solution(order) {
    let o_li = String(order).split('')
    let answer = 0
    o_li.forEach(s => {
        if (s == '3' ||s == '6'|| s == '9' ) {
            answer += 1
        }
    })
    return answer;
}