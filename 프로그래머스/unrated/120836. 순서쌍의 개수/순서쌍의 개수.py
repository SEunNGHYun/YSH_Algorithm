def solution(n):
    sqrt_n = int(n ** 0.5)
    count = 0
    for num in range(1, sqrt_n + 1):
        if n % num == 0:
            count += 2
    if sqrt_n * sqrt_n  == n :
        count -= 1
            
    return count 