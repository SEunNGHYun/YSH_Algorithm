def solution(n):
    ob = bin(n)
    count_one = ob.count('1')
    result = n + 1
    result_ob = bin(result)
    while True:
        if (result_ob.count('1') == count_one):
            break
        
        result += 1
        result_ob = bin(result)
    return result