function solution(k, m, score) {
    var len = score.length;
    score.sort()
    let money = 0
    while (len - m >= 0) {
        money += score.slice(len-m,len)[0] * m
        len -= m
    }
    return money
}