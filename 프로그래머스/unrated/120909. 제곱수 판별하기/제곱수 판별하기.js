function solution(n) {
    var m = Math.floor(Math.sqrt(n));
    return (m*m) == n ? 1 : 2;
}