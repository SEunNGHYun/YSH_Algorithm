function solution(maps) {
    const moves = [[0,1], [1,0], [-1, 0], [0, -1]]
    const n = maps[0].length, m = maps.length;
    let visited = []
    for(let k = 0; k < m; k++){
        visited[k] = Array(n).fill(0)
    }
    let q = [[0, 0]]
    visited[0][0] = 1
    
    while (q.length > 0) {
        let [i, j] = q.shift()
        
        moves.forEach((move) => {
            let [mi, mj] = move
            let xi = mi + i, xj = mj + j;
            if(0<=xi && xi<m && 0<=xj && xj<n){
                if(!visited[xi][xj] && maps[xi][xj]){
                    visited[xi][xj] = visited[i][j] + 1
                    q.push([xi, xj])
                }}
        })
    }
    return (visited[m-1][n-1] ) ?  visited[m-1][n-1] : -1
}