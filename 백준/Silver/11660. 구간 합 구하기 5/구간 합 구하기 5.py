import sys

input = sys.stdin.readline
n, m = map(int, input().split())
n_m = []
n_m_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n):
  n_m.append(list(map(int, input().split())))
  
for i in range(1, n+1) :
  for j in range(1, n+1):
    n_m_sum[i][j] = n_m_sum[i][j-1] + n_m_sum[i-1][j] - n_m_sum[i-1][j-1] + n_m[i-1][j-1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(n_m_sum[x2][y2] + n_m_sum[x1 - 1][y1 - 1] - n_m_sum[x2][y1-1] - n_m_sum[x1-1][y2])
