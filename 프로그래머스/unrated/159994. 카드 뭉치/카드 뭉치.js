function solution(cards1, cards2, goal) {
    let answer = 'Yes', j = 0, result = [];
    goal.forEach((s, i) => {
        if(cards1[0] == s){
            result.push(cards1.shift())            
        }else if (cards2[0] == s)
            result.push(cards2.shift())
    })
    if(result.length == goal.length){
        result.forEach((s, i) => {
            if (goal[i] != s) {
                answer = 'No'
                return
            }
        })
    }else {
        answer = 'No'
    }
    return answer
}