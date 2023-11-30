function solution(a, b) {
    let answer = 1
    for(let c = b; c > 1; c--){
        if (a % c == 0 && b % c == 0){
            b /= c
            break
        }
    } // 기약 분수의 분모만 구함
    
    while ((b % 2 == 0) || (b % 5 == 0)){
        if ((b % 2 == 0)) b /= 2
        if ((b % 5 == 0)) b /= 5
    } // b의 약수가 2 또는 5만으로 이루어져 있는 확인
    
    if (b == 1){
        return 1
    }else{
        return 2
    }
}