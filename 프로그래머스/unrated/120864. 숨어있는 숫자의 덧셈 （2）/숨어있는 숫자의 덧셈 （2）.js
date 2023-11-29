function solution(my_string) {
    let nums = ['1', '2', '3', '4', 
               '5', '6', '7', '8',
               '9', '0']
    let save = ''
    let answer = 0
    for (let i = 0; i < my_string.length;i++){
        
        if(nums.includes(my_string[i])){
           save += my_string[i]
        }else{
            if(save !== ''){
                answer += Number(save)
            }
            save = ''
        }
    }
    if(save !== ''){
      answer += Number(save)
    }
    return answer;
    
}