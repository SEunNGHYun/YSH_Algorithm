function solution(array, n) {
    let compare = Math.abs(n-array[0])
    let answer = array[0]
    for (let i = 1; i < array.length; i++){
        var c = Math.abs(n-array[i])
        if (compare > c){
            answer = array[i]
            compare = c
        }else if (compare == c) {
            if (answer > array[i]){
                answer = array[i]
            }
            compare = c
        }
    }
    return answer
}