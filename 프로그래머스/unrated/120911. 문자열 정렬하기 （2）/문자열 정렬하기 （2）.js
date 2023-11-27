function solution(my_string) {
    var answer = my_string.split('').map((s) => s.toLowerCase()).sort((a,b) => a > b ? 1 : -1).join('');
    return answer;
}