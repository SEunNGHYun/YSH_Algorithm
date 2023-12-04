function solution(bin1, bin2) {
    bin1 = parseInt(bin1, 2)
    bin2 = parseInt(bin2, 2)
    
    let b2 = bin2 + bin1
    
    return b2.toString(2)
}