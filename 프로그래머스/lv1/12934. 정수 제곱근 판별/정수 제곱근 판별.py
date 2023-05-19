def solution(n):
    val = round(n ** (0.5))
    if (val * val) == n:
        return (val + 1) ** (2)
    else:
        return -1