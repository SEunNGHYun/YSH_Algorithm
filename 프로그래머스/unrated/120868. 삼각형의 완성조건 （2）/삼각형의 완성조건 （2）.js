function solution(sides) {
    var lng=0, sht = 0, answer = 0;
    let save = 0
    if (sides[1] >= sides[0]){
        lng = sides[1]
        sht = sides[0]
    }else{
        lng = sides[0]
        sht = sides[1]
    }
    console.log(sht, lng)
    for (let n = 1; n <= lng; n++){
        if ((n + sht) > lng){
            answer += 1
            save = n
        }
    }
    return (((lng+sht) - 1) - save) + answer;
}