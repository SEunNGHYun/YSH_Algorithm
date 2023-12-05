function solution(num, total) {
    let answer = []
    let n=0
    while (true) {
        let check = 0, save = []
        for (let m = (n-num); m < n; m++) {
            check += m
            save.push(m)
        }
        if (check == total) {
            answer = save
            break
        }
        n++
    }
    return answer
}