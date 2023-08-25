function solution(dartResult) {
    let dart = dartResult.split('');
    let j = 0;
    let score = 0, record = 0, result = 0
    for(let i = 0; i < dart.length; i++){
        if(dart[i] == 'S' || dart[i] == 'D' || dart[i] == 'T'){
            if(dart[i] == 'S'){
                score = Math.pow(score, 1)
            }else if(dart[i] == 'D') {
                score = Math.pow(score, 2)
            }else{
               score = Math.pow(score, 3)
           } 
        }else if(dart[i] == '*' || dart[i] == '#'){
            if(dart[i] == '*'){
                score *= 2
                result += record
                record = 0
            }else{
                score *= (-1)
                record = 0
            }
        }else {
            result += score            
            record = score
            if(dart[i] == '1' && dart[i+1] == '0'){
                score = 10
                ++i
            }else{
                score = Number(dart[i])
            }
        }
    }

    result += score
    
    return result
}