function solution(polynomial) {
    polynomial = polynomial.split(' + ')
    let poly = 0, num = 0
    polynomial.forEach(p => {
            if(p.includes('x')){
                if (p === 'x') {
                    poly += 1
                }else{
                    poly += Number(p.slice(0, -1))
                }
            }else{
                num += Number(p)
            }
    })
    if (num === 0){
        return (poly === 1 ? '' : poly) + 'x'
    }else if (poly === 0){
        return '' + num
    }else{
        return (poly === 1 ? '' : poly )+ 'x' + ' + ' + num
    }
    // return answer;
}