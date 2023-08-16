function solution(k, dungeons) {
    const LENG = dungeons.length;
    let answer = []; 
    var visited = Array(LENG).fill(false);
    
    function DFS(deep, hp) {
        
        answer.push(deep)
        
        for (let i = 0; i < LENG; i++) {
            if (!visited[i] & dungeons[i][0] <= hp) {
                
                visited[i] = true
                DFS (deep + 1, hp - dungeons[i][1])
                visited[i] = false
            }
        }
    }
    
    DFS (0, k)
    return Math.max(...answer);
}