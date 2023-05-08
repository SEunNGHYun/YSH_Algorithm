function solution(arr) {
    var sum = arr.reduce((a,b) => a + b)
    return sum / (arr.length) ;
}