function solution(progresses, speeds) {
    let proccess = progresses.map((w) => (100 - w));
    let done = proccess.map((w, i) => Math.ceil(w / speeds[i]));
    let result = []
    let w_time = done[0], w_count = 1
    for (let i = 1; i < done.length; i++){
        if(w_time < done[i]){
            w_time = done[i]
            result.push(w_count)
            w_count = 1
        }else{
            w_count += 1
        }
    }
    result.push(w_count)
    console.log(done)
    console.log(result)
    
    return result
    
    
}