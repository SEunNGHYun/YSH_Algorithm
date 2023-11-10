def solution(babbling):
    speak = ["aya", "woo", "ye", "ma"]
    answer = 0
        
    for s in babbling: 
        ong = ''
        for ss in s : 
            ong += ss
            if ong in speak :
                ong = ''
        if ong == '':
            answer += 1
    return answer