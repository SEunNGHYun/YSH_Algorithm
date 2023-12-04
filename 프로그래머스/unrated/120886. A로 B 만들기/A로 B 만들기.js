function solution(before, after) {
    before = before.split('')
    after = after.split('')
    let answer = 1
    for(let i = 0; i < before.length; i++){
        let idx = after.indexOf(before[i])
        if (idx >= 0){
            after[idx] = ''
        }else{
            answer = 0
            break
        }
    }
    
    return answer; 
}