def solution(number):
    leng = len(number)
    count = 0
    for i in range(leng-2):
        for j in range(i+1,leng-1):
            for k in range(j+1, leng):
                if (number[i] + number[j] + number[k]) == 0:
                    count += 1
    return count
    