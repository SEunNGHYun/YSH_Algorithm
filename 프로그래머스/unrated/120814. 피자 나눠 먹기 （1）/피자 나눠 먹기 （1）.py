def solution(n):
    pi = int(n / 7)
    d = n % 7
    if (d > 0):
        pi += 1
    return pi