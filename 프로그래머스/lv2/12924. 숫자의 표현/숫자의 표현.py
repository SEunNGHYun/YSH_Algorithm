def solution(n):
    answer = 1
    
    for i in range(1, n):
        sum_val = i
        val = i + 1
        while sum_val < n :
            sum_val += val 
            val += 1
        if sum_val == n:
            answer += 1
    return answer