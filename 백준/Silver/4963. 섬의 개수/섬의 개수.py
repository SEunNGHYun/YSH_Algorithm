import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
result = []
move = ((0,1), (1,0), (-1, 0), (0, -1), (1,1), (1, -1), (-1, -1), (-1, 1))
while n > 0 and m > 0:
  feild = []
  visited = [[0] * n for _ in range(m)]
  count = 0
  
  for _ in range(m):
    feild.append(list(map(int, input().strip().split())))

  for i in range(m):
    for j in range(n):
      if visited[i][j] == 0 and feild[i][j] == 1:
        count += 1
        
        q = deque([(i, j)])
        visited[i][j] = 1
        while q :
          ci, cj = q.popleft()
          
          for mi, mj in move :
            xi, xj = (mi + ci), (mj + cj)
            if 0<=xi<m and 0<=xj<n and visited[xi][xj] == 0 and feild[xi][xj] == 1:
              q.append((xi, xj))
              visited[xi][xj] = 1
              
  result.append(count)
  n, m = map(int, input().split())
  
for val in result:
  print(val)