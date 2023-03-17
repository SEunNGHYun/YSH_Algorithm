import sys

input = sys.stdin.readline

n, s = map(int, input().split())
n_li = list(map(int, input().split()))


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


dis = []
for i in range(n):
    dis.append(abs(s-n_li[i]))

com = dis[0]
for i in range(1, n):
    com = gcd(dis[i], com)
print(com)
