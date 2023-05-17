function solution(phone_number) {
    var len = phone_number.length - 4
    var answer = ''
    for(let n = 0; n < len ; n++) {
        answer += '*'
    }
    answer += phone_number.slice(len);
    return answer
}