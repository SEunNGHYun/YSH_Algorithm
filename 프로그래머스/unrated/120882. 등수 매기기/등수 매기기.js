function solution(score) {
    let avgLi = score.map(([m,e]) => (m+e)/2)
    let leng =  avgLi.length
    let answer = avgLi.map((score, i) => {
        let rank = 0
        for(let j = 0; j < leng; j++){
            if (score >= avgLi[j]){
                rank += 1
            }}
            return (leng - rank) + 1
        })
    return answer
}