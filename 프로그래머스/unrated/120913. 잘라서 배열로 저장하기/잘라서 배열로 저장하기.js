function solution(my_str, n) {
    let leng = my_str.length
    my_str = my_str.split('')
    var answer = [];
    for (let j = 0; j < leng; j=j+n){
        answer.push(my_str.splice(0, n).join(''))
    }
    return answer;
}