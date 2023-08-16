function solution(answers) {
    const one = [1, 2, 3, 4, 5], two = [2, 1, 2, 3, 2, 4, 2, 5],
          three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] ;
    let answer = [0, 0, 0]
    answers.forEach((a, i) => {
        if (a == one[i % 5]){
            answer[0] += 1
        }
        if (a == two[i % 8]){
            answer[1] += 1
        }
        if (a == three[i % 10]){
            answer[2] += 1
        }
    })
    let max_answer = Math.max(...answer)
    let result = []
    answer.forEach((a, i) => {
        if(a == max_answer){
            result.push(i + 1)
        }
    })
    return result
}