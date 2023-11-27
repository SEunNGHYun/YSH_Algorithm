function solution(array) {
    let count = 0
    array = array.map(n => String(n))
    array.forEach(ns => {
        ns.split('').forEach(s => s == '7' && ++count)
    })
    return count
}