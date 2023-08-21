function solution(name, yearning, photo) {
    let name_yearing = {}
    name.forEach((n, i) => {
        name_yearing[n] = yearning[i]
    })  
    return photo.map(names => {
        let sum_yearning = 0;
        names.forEach((n, i) => {
            if (n in name_yearing){
                sum_yearning += name_yearing[n] 
            }
        }) 
        return sum_yearning;
    })
} 