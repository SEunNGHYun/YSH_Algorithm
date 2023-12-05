function solution(A, B) {
    let answer = -1
    for (let i = 0; i< A.length; i++){
        let compare = B.slice(i) + B.slice(0, i)
        if (compare === A) {
            answer = i
            break
        }
    }
    return answer
}