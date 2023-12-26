function solution(s) {
    let ss = {}
    let key = ''
    for(let i=1; i < (s.length - 1); i++) {
        if ((s[i] != ',') && (s[i] != '}') && (s[i] != '{')){
            key += s[i]
        }else {
            if (key != '') {
                if (!Object.keys(ss).includes(key)) {
                    ss[key] = 1
                }else{
                    ss[key] += 1
                }
            }
            key = ''
        }
    }
    let vals = Object.values(ss).sort((a,b) => b-a)
    let answer = []
    for (let v of vals) {
        answer.push(Number(Object.keys(ss).find(key => ss[key] === v)))
    }
    console.log(vals)
    
    return answer
}