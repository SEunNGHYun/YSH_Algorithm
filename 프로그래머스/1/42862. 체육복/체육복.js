function solution(n, lost, reserve) {
    var arr = Array(n).fill(1)
    var answer = 0
    
    lost.forEach(ele => arr[ele-1]-= 1)
    reserve.forEach(ele=>arr[ele-1] += 1)
    
    arr.forEach((ele, i) => {
        if (ele === 0) {
            if (i - 1 >= 0) {
                if(arr[i-1] === 2) {
                    arr[i] = 1
                    arr[i-1] = 1
                    return
                }
            }
            if (i + 1 < n) {
                if(arr[i+1] === 2) {
                    arr[i] = 1
                    arr[i+1] = 1
                    return
                }
            }
        }
    })
    arr.forEach(ele => ele >= 1 && answer++)
    return answer
}