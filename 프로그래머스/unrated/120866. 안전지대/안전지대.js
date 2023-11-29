function solution(board) {
    let w = board.length
    var saveZone = w * w;
    
     function check (fi, fj){
        let move = [[-1, -1], [-1, 0], [-1, 1], 
                    [0, -1], [0, 1], 
                    [1, -1], [1, 0], [1, 1]]
                    
        for (let j = 0; j < move.length; j++){
                let mii = fi+move[j][0], mjj = fj+move[j][1]
                if ((mii< w && 0 <= mii) && (mjj< w && 0 <= mjj)){
                    if (board[mii][mjj] == 0){
                        board[mii][mjj] = -1
                        saveZone -= 1
                    }
                }
            }
    }
    for (let i = 0; i < w;i++){
        if (board[i].includes(1)){
            for (let j = 0; j < w; j++){
                if (board[i][j] === 1){
                    check(i, j)
                    saveZone -= 1
                }
            }
        }
    }
    
   
    
    return saveZone;
}