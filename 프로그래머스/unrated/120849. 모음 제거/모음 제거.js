function solution(my_string) {
    var moum = ["a", "e", "i", "o", "u" ];
    var check_i
    var answer = ''
    for (let i = 0; i < my_string.length;i++){
        check_i = moum.indexOf(my_string[i])
        if (check_i == -1){
            answer += my_string[i]
        }
    }
    return answer
}