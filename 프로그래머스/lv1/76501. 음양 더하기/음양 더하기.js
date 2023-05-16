function solution(absolutes, signs) {
    var result = 0;
    for (let i = 0; i < absolutes.length; i++) {
        if (signs[i]){
            //true
            result += absolutes[i]
        }else{
            //false
            result = result + (absolutes[i] * (-1))
        }
    }
    return result;
}