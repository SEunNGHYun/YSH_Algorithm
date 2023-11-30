function solution(n) {
    let count = 1
    let numX3 = 1
    while (count < n) {
        numX3 += 1
        if (((numX3 % 3) === 0) || String(numX3).indexOf('3') >= 0){
            continue
        }
        count += 1
    }
    console.log(numX3)
    return numX3
}