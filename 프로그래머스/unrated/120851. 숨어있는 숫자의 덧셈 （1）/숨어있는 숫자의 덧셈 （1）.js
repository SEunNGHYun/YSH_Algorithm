function solution(my_string) {
    var nums = my_string.split('');
    var result = 0
    nums.forEach((a) => {
        if(Number(a) >= 0){
            result += Number(a)
        }
    })
    return result
}