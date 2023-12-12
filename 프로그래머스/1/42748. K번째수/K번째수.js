function solution(array, commands) {
    let result = commands.map(arr => {
        console.log(array.slice(arr[0]-1, arr[1]))
        return array.slice(arr[0]-1, arr[1]).sort((a,b)=>a-b)[arr[2] -1]
    })
    
    return result
}