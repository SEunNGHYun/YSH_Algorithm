function solution(s) {
    let s_li = s.split(' ')
    let last = null
    let answer = 0
    s_li.forEach(s => {
        if (s == 'Z'){
            answer -= last
        }else{
            answer += Number(s)
            last = s
        }
    })
    return answer
}