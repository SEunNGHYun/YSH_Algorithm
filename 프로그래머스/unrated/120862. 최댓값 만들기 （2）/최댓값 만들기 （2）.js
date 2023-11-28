function solution(numbers) {
    var answer = numbers[0] * numbers[1];
    numbers.forEach((n, i) => {
        for (let j = i + 1; j < numbers.length; j++){
            if(answer < numbers[j] * n){
                answer = numbers[j] * n
            }
        }
    })
    return answer;
}