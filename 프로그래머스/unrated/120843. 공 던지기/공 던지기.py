def solution(numbers, k):
    leng = len(numbers)
    i = 0
    if leng % 2 == 0:
        k -= 1
        while k > 0:
            k -= 1
            i += 2
            if i == leng:
                i = 0
    else: 
        while k > 1:
            k -= 1
            i += 2
            if i == leng :
                i = 0
            elif i == leng + 1:
                i = 1
    return numbers[i]
            
            
        