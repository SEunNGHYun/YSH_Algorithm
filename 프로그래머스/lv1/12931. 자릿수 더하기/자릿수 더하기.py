def solution(n):
    str_n = str(n)
    index_n = len(str_n) - 1
    answer = 0
    while index_n >= 0:
        answer += int(str_n[index_n])
        index_n -= 1
    return answer