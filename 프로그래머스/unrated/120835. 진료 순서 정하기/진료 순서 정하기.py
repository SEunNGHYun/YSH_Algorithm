def solution(emergency):
    answer = []
    for e1 in emergency:
        turn = 1
        for e2 in emergency:
            if (e1 < e2):
                turn +=1
        answer.append(turn)
                
    return answer