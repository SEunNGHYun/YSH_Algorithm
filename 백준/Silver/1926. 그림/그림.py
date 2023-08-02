import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
feild = []

for _ in range(n):
  feild.append(list(map(int, input().split())))

move = [(0,1), (-1, 0), (1, 0), (0, -1)]
big, size, cnt = 0, 0, 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if (not visited[i][j]) and (feild[i][j] == 1):
      cnt += 1
      size = 1
      q = deque([(i, j)])
      visited[i][j] = True
      
      while q:
        xi, xj = q.popleft()
        
        for mi, mj in move:
          ci, cj = (xi + mi), (xj + mj)
          if 0<=ci<n and 0<=cj<m :
            if (feild[ci][cj] == 1) and (not visited[ci][cj]):
              q.append((ci, cj))
              size += 1
              visited[ci][cj] = True
      if size > big:
        big = size
        
print(cnt)
print(big)