function solution(x) {
    var s = 0 
    String(x).split('').forEach(n => s += Number(n))
    return x % s == 0 ? true : false
}