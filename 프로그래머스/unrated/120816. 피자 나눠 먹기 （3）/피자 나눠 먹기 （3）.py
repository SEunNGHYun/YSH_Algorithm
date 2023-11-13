def solution(slice, n):
    result = 0
    for i in range(1, 100):
        if (slice * i) >= n :
            result = i
            break
    return result