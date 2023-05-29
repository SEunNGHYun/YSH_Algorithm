def solution(d, budget):
    answer = 0
    d.sort()
    for p in d:
        if budget - p >= 0:
            budget -= p
            answer += 1
    return answer
