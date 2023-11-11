def solution(n, k):
    drink = int(n / 10)
    return (n * 12000) + ((k - drink) * 2000)