function solution(numbers) {
    const leng = numbers.length 
    numbers.sort((a, b) => a-b)
    return numbers[leng-1] * numbers[leng-2]
}