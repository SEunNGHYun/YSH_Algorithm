function solution(keyinput, board) {
    var answer = [0, 0];
    const w = Math.floor(board[0]/2), h = Math.floor(board[1]/2)
    keyinput.forEach(key => {
        if(key == 'left'){
            if (answer[0] > w * (-1)){
                answer[0] -= 1
            }
        }else if (key == 'right'){
            if (answer[0] < w){
                answer[0] += 1
            }
        }else if (key == 'up'){
            if (answer[1] < h){
                answer[1] += 1
            }
        }else if (key == 'down'){
            if (answer[1] > h * (-1)){
                answer[1] -= 1
            }
        }
    })
    return answer;
}