function solution(dots) {
    let check = dots[0]
    let w = dots[0][0], h = dots[0][1]
    
    dots.forEach(d => {
        if (check[0] != d[0]){
            w = d[0]
        }
        if (check[1] != d[1]){
            h = d[1]
        }
    })
    return Math.abs(w-check[0]) * Math.abs(h-check[1])
}