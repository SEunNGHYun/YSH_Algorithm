import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    P = [1 for _ in range(n)]
    for i in range(3, n):
        P[i] = P[i-2] + P[i-3]
    print(P[n-1])
