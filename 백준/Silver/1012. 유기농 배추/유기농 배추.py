import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
  m, n, k = map(int, input().split())
  feild = [[0] * m for _ in range(n)]
  visited = [[0] * m for _ in range(n)]
  bug = 0
  for _ in range(k):
    x, y = map(int, input().split())
    feild[y][x] = 1
  
  for i in range(n):
    for j in range(m):
      if (not visited[i][j]) and (feild[i][j] == 1):
        q = deque([(i, j)])
        visited[i][j] = True
        bug += 1
        
        while q:
          ci, cj = q.popleft()
          
          for mi, mj in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            xi, xj = (ci + mi), (cj + mj)
            if 0<=xi<n and 0<=xj<m : 
              if (feild[xi][xj] == 1) and (not visited[xi][xj]):
                q.append((xi, xj))
                visited[xi][xj] = True
        
  result.append(bug)

for b in result:
  print(b)