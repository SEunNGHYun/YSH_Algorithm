function solution(n, numlist) {
    var answer = numlist.filter((num) => {
        if (num % n == 0) {
            return num
        }
    })
    return answer;
}