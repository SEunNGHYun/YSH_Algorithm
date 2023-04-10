import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v = int(input())
    # 센트를 달러로 변경 1센트는 0.01달러
    q = v // 25
    d = (v % 25) // 10
    n = ((v % 25) % 10) // 5
    p = (((v % 25) % 10)) % 5
    print(q, d, n, p)
