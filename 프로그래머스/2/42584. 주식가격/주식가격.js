function solution(prices) { 
    let answer = []
    for(let i = 0; i < prices.length; i++){
       let com = prices[i], count = 0
       for (let j = i+1; j < prices.length; j++){
           count++
           if(com > prices[j]) break
       }
       answer.push(count)
   }
   return answer
}