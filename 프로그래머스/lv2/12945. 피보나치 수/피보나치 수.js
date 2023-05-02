function solution(n) {
  let val = [0, 1, 1, 2] 
  let arr = []
  if (n > 4){
    arr = new Array(n - 4);
  }
  for(let i = 4; i <= n ; i++){
    val[i] = (val[i-1] + val[i-2]) % 1234567;
  }
  return val[n] ;
}


console.log(solution(10000))