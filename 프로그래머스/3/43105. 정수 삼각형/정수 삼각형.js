function solution(triangle) {
    let answer = 0, last = 0
    for(let i = 1; i < triangle.length; i++){
        for(let j = 0; j < i+1; j++) {
            if (j == 0) {
                triangle[i][j] += triangle[i-1][0]
            }else if (j == triangle[i].length) {
                triangle[i][j] += triangle[i-1][j-1]
            }else{
                if (triangle[i-1][j] > triangle[i-1][j-1]) {
                    triangle[i][j] += triangle[i-1][j]
                }else{
                    triangle[i][j] += triangle[i-1][j-1]
                }
            }
        }
        last = i
    }
    return Math.max(...triangle[last])
}