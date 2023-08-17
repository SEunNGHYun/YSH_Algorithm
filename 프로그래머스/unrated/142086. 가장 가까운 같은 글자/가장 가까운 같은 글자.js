function solution(s) {
    let answer = [-1]
    
    for (let i = 1; i < s.length; i++){
        
        for(let j= i - 1; j >= 0; j--){
            if (s[j] == s[i]) {
                answer.push(i-j)
                break
            }else if(j == 0){
                answer.push(-1)
            }
        }
    }
    return answer
}