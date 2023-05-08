function solution(arr) {
    let min = Infinity;
    let answer = [];
    arr.forEach(ele => {
        if(ele < min){
            min = ele
    }})
    arr.forEach(ele => {
        if(ele != min){
            answer.push(ele)
    }})
    if(answer.length == 0){
        answer.push(-1)
    }
    return answer 
}