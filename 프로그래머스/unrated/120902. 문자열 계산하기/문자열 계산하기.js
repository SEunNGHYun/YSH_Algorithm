function solution(my_string) {
    let s_li = my_string.split(' ')
    let answer = Number(s_li[0])
    let isAdd = true
    console.log(s_li)
    for (let i = 1;i < s_li.length; i++){
        if(s_li[i] != '+' && s_li[i] != '-'){
            if (isAdd){
                answer += Number(s_li[i])
            }else{
                answer -= Number(s_li[i])
            }
        }else{
            if(s_li[i] == '+'){
                isAdd = true
            }else if (s_li[i] == '-') {
                isAdd = false
            }
        }
    }
    return answer
}