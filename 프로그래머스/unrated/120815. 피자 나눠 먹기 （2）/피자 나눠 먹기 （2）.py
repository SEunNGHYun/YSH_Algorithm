def solution(n):
    m = 6
    while True :
        if (m % n == 0):
            break
        else :
            m += 6
            
    return m // 6