function solution(k, score) {
    let li = []
    let answer = []
    for(let i = 0; i < score.length; i++){
            if (i < k) {
                li.push(score[i])
                li.sort((a,b) => b-a)
            }
            else if(score[i] > Math.min(...li)){
                    li.pop()
                    li.push(score[i])
                    li.sort((a,b) => b-a)
            }
            answer.push(li[li.length-1])
    }    
    return answer;
}