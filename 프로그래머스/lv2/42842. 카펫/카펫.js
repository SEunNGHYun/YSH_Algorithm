function solution(brown, yellow) {
    let answer = [0, 0]
    
    for (let w = 1; w <= yellow; w++){
        let h = Math.floor(yellow/w)
        
        if(w >= h) {
            let size = (w*2) + (h*2) + 4;
            
            if (brown == size) {
                answer = [w + 2, h + 2]
                break
            }
        }
    }
    
    
    return answer
}