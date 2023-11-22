function solution(my_string) {
    let s_set = new Set(my_string.split(''))
    let arr = [...s_set]
    
    return arr.join("")
}