

function numCheck(num) {
        num = Number(num)
        let sNum = Math.floor(num ** 0.5)
        let count = 0;

        for (let n = 2; n <= sNum; n++){
            if (num % n == 0) count ++
        }
        if (num == 1 || num == 0) return false
        else if(count >= 1) return false
        return true
    }
  
        
function solution(numbers) {
    let nums = numbers.split('')
    let answer = new Set()
    function dfs (s, arr, num) {
        if (arr.length >= 1){
            for (let i = 0; i < arr.length; i++){
                let n = num + arr[i]
                let c_arr = [...arr]
                //i 인덱스 제거
                c_arr.splice(i, 1)
                
                if (numCheck(n)) {
                    s.add(Number(n))
                }
                dfs(s, c_arr, n)
            }
        }
    }
    dfs(answer, nums, '')   
    return answer.size;
}