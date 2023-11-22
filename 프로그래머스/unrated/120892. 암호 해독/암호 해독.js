function solution(cipher, code) {
    var answer = '';
    cipher = ' ' + cipher
    for (let i = code; i < cipher.length; i = i+code){
        answer += cipher[i]
    }
    return answer;
}