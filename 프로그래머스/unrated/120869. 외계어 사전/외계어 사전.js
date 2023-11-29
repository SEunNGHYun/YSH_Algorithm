function solution(spell, dic) {
    var answer = 2;
    let count = 0
    for (const d of dic) {
        count = 0
        for (let s of spell){
            if (d.indexOf(s) >= 0){
                if (d.indexOf(s) === d.lastIndexOf(s)){
                    count += 1
                }
            }
        }
        console.log(count)
        if (count == spell.length){
            answer = 1
            break
        }
    }
    return answer;
}