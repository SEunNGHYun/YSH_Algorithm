def solution(brown, yellow):
    #가로 >= 세로
    answer = []
    num = int(yellow ** 0.5)
    w = 1
    h = 1
    for n in range(1,num+1):
        print(n)
        if ((n*2) + ((yellow // n) * 2) + 4) == brown:
            w = yellow // n
            h = n
        
    answer = [w+2, h+2]
    return answer