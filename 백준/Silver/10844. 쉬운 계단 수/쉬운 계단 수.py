import sys

input = sys.stdin.readline

n = int(input())

li = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + \
    [[0 for _ in range(10)] for _ in range(n-1)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            li[i][j] = li[i-1][1]
        elif j == 9:
            li[i][j] = li[i-1][8]
        else:
            li[i][j] = li[i-1][j-1] + li[i-1][j+1]

print(sum(li[n-1]) % 1000000000)

