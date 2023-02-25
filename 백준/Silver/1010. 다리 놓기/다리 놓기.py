import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    facto = [1, 1, 2, 6]  # 0! ~ 3!

    if m >= 4:
        for i in range(4, m+1):
            facto.append(i * facto[i-1])

    print(facto[m] // (facto[n] * facto[m-n]))
