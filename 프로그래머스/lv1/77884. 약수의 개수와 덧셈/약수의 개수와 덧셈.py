def solution(left, right):
    answer = 0
    def aksu_even_check (n):
        count = 1
        for num in range(1,n):
            if(n % num) == 0:
                count += 1
        if (count % 2) == 0:
            return True
        else:
            return False
    for num in range(left, right+1):
        if aksu_even_check(num):
            answer += num
        else:
            answer -= num
    return answer