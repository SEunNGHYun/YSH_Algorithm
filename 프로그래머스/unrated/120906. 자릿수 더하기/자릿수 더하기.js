function solution(n) {
    var answer = 0
    String(n).split('').forEach(num => {
        answer += Number(num)
    });
    return answer;
}