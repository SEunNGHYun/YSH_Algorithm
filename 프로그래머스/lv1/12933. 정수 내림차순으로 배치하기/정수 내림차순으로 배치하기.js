function solution(n) {
    var str_n = String(n).split('');
    var num_n = str_n.map((a) => Number(a))
    num_n.sort(function (a,b) {
        return b - a;
    })
    num_n = Number(num_n.join(''))
    return num_n;
}