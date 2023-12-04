function solution(i, j, k) {
    let answer = 0
    for (;i<= j; i++){
        let s_li = String(i).split('')
        if(s_li.indexOf(String(k)) >= 0){
            s_li.forEach(s => s == k && answer++)
        }
    }
    return answer 
}