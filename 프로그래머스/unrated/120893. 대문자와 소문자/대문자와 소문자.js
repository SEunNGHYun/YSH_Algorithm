function solution(my_string) {
    let answer = ''
    for (let i = 0; i < my_string.length;i++){
        var asc2 = my_string.charCodeAt(i)
        if (65 <= asc2 && asc2 <= 90){
            answer += my_string[i].toLowerCase()
        }else if (97 <= asc2 && asc2 <= 122) {
            answer += my_string[i].toUpperCase()
        }
    }
    return answer
}