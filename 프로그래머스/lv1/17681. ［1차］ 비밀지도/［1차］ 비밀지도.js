function solution(n, arr1, arr2) {
    let result = []
    
    for (let i = 0; i < n; i++){
        let bin_a = arr1[i].toString(2), bin_b = arr2[i].toString(2);
        let a_leng = bin_a.length, b_leng = bin_b.length
        let n_fill_a = Array(n-a_leng).fill(0).join(''), 
            n_fill_b = Array(n-b_leng).fill(0).join('')
            bin_a = n_fill_a + bin_a, bin_b = n_fill_b+bin_b
        let feild_n = ''
        for(let j = 0; j < n; j++){
            if(bin_a[j] == '1' || bin_b[j] == '1'){
                feild_n += '#'
            }else{
                feild_n += ' '
            }
        }
        result.push(feild_n)
    }
    return result
}