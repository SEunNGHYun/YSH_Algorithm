function solution(citations) {
    let bool = true;
    let Hindex = 0;
    citations.sort((a, b) => b-a).forEach((num, index)=> {
        if(num <= index && bool == true){
            console.log("inde",index)
            bool = false
            Hindex = index;
        }else if (bool == true){
            Hindex = index + 1;
        }
    });
    console.log(Hindex)
    
    return Hindex;
}