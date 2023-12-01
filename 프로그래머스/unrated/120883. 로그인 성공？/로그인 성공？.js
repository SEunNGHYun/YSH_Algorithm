function solution(id_pw, db) {
    let [id, pw] = id_pw
    let answer = 'fail'
    db.forEach(([ids, pws]) => {
        if (ids === id){
            if(pws === pw){
                answer = 'login'
                return
            }else{
                answer = "wrong pw"
                return
            }
        }
    })
    
    return answer
}