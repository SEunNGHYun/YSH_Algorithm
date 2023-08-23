function solution(priorities, location) {
    let process = [], result = []
    let front = 0, max = 0
    
    for (let i = 0; i < priorities.length; i++){
        process.push(i)
    }
    
    while (priorities.length > 0) {
        front = priorities.shift()
        max = Math.max(...priorities)
        if(front < max) {
            priorities.push(front)
            process.push(process.shift())
        }else{
            result.push(process.shift())
        }
    }
    for (let i = 0; i < result.length;i++){
        if(result[i] == location){
            return i+1;
        } 
    }
}