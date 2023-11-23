function solution(s) {
    let check = {}
    var answer = [];
    for (let i = 0; i < s.length; i++){
        if (s[i] in check){
            check[s[i]] += 1
        }else{
            check[s[i]] = 1
        }
    }
    for (key in check){
        if (check[key] === 1){
            answer.push(key)
        }
    }
    answer.sort((a, b) => a.localeCompare(b))
    return answer.join('');
}