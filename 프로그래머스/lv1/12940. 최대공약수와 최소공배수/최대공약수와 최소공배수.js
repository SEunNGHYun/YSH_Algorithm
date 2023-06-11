function solution(n, m) {
    let bucket = 0
    if (n > m) {
        bucket = m
        m = n
        n = bucket
    } // n이 작은 수 m이 큰 수 
    let gcd_val = gcd(n, m)
    let lcm_val = lcm(n, m,gcd_val)
    let result = [gcd_val,lcm_val]
    return result
}

function gcd(a, b) {
    let divi = -1

    while (divi != 0) {
        divi = a % b
        a = b
        b = divi
    }
    
    return a
}

function lcm(a, b, gcd) {
    return (a * b) / gcd
}