function solution(want, number, discount) {
    let want_obj = {}
    let result = 0;
    want.forEach((w, i) => {
        want_obj[w] = number[i]
    })
    discount.forEach((o,i)=> {
        let copy_obj = {...want_obj};
        for(let j = i; j < i+10; j++){
            if (discount[j] in copy_obj){
                if(copy_obj[discount[j]] > 0){
                    copy_obj[discount[j]] -= 1
        }}}
        let check = false
        Object.values(copy_obj).forEach(v => {
        if(v != 0){
            check = true;
            return
        }})
        if (!check){
            result += 1;
        }
    })
    return result
}