import sys

input = sys.stdin.readline

n = int(input())
n_tree = []

for _ in range(n):
    leaf = list(map(int, input().split()))
    n_tree.append(leaf)

# 깊이가 증가할 때 마다 깊이값 만큰의 배열크기가 지정된다.
dp = [[0 for _ in range(i)] for i in range(1, n+1)]
dp[0][0] = n_tree[0][0]  # 첫 번째 요소 넣어서 시작

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + n_tree[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + n_tree[i][j]
        else:
            # 이전 depth의 값을 현재 depth의 2개의 값과 비교하여 큰값 넣기
            com1 = dp[i-1][j-1] 
            com2 = dp[i-1][j] 
            if com1 > com2:
                dp[i][j] = com1 + n_tree[i][j]
            else:
                dp[i][j] = com2 + n_tree[i][j]
print(max(dp[n-1]))
