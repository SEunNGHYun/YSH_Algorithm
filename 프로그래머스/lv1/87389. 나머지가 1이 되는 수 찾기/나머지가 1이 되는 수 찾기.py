def solution(n):
    n -= 1 
    sq_n = int(n ** 0.5)
    print("!!! :", sq_n)
    result = 0
    for num in range(2, sq_n+1):
        if n % num == 0:
            print("???: " , num)
            result = num
            break
    if result == 0 :
        result = n
            
    return result        