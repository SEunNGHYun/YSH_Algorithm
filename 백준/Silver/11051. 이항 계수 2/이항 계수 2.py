import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] for i in range(n+1)]

dp[1].append(1)  # 현재 dp == [[1], [1,1]]

for i in range(2, n+1):
    for j in range(1, i+1):
        if j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])


print(dp[n][k] % 10007)
