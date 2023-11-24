function solution(array) {
    let arr = array.slice()
    array.sort((a,b) => b-a)
    return [array[0], arr.indexOf(array[0])]
}