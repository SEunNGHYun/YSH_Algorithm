function solution(sizes) {
    let maxW = 0
    let maxH = 0
    let all = sizes.map(([w, h]) => {
        if(w > h) return [w, h]
        else return [h, w]
    })
    all.forEach(([w, h]) => {
        maxW = Math.max(maxW, w)
        maxH = Math.max(maxH, h)
    })
    return maxW * maxH
}