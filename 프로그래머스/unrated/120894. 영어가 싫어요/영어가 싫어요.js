function solution(numbers) {
    var nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let i = 0
    let answer = ''
    while (i < numbers.length) {
        if (numbers[i] == 'z'){
            answer += '0'
            i += 4
        }else if(numbers[i] == 'o'){
            answer += '1'
            i += 3
        }else if(numbers[i] == 't'){
            if (numbers[i+1] == 'w') {
                answer += '2'
                i += 3
            } else if(numbers[i+1] == 'h') {
                answer += '3'
                i += 5
            }
        }else if(numbers[i] == 'f'){
           if (numbers[i+1] == 'o') {
                answer += '4'
            } else if(numbers[i+1] == 'i') {
                answer += '5'
            }
            i += 4
        }else if(numbers[i] == 's'){
           if (numbers[i+1] == 'i') {
                answer += '6'
                i += 3
            } else if(numbers[i+1] == 'e') {
                answer += '7'
                i += 5
            }
        }else if(numbers[i] == 'e'){
            answer += '8'
            i += 5
        }else if(numbers[i] == 'n'){
            answer += '9'
            i += 4
        }
    }
    return Number(answer);
}