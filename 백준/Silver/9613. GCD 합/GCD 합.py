import sys

input = sys.stdin.readline

t = int(input())


def gcd(n, m):
    big = small = mid = 0
    result = 0
    if n > m:
        big = n
        small = m
    else:
        big = m
        small = n

    while True:
        mid = small
        small = big % small
        big = mid
        if small == 0:
            result = big
            break
    return result

for _ in range(t):
    val_li = list(map(int, input().split()))
    leng = val_li[0]
    result = 0
    for i in range(1, leng):
        for j in range(i+1, leng+1):
            result += gcd(val_li[i], val_li[j])
    print(result)
