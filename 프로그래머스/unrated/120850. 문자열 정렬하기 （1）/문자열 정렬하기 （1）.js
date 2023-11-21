function solution(my_string) {
    var nums = []
    var my_strings = my_string.split('')
    my_strings.forEach((s, i) => {
        if (Number(s) >= 0){
            nums.push(Number(s))
        }
    })
    nums.sort((a,b) => a-b)
    return nums
}