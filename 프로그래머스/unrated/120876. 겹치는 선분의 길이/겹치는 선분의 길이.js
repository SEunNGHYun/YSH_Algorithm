function solution(lines) {
    let lngs = new Array(200).fill(0), answer = 0
    lines.forEach((line, index) => {
        let [start, end] = line
        for (let i = (start + 100); i < (end+100); i++){
            lngs[i] += 1
        }
    })
    lngs.forEach((l, i) => {
        if (l >= 2){
            answer += 1
        }
    })
    return answer
}