import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
feild = []

for _ in range(n):
  feild.append(list(map(int, input().strip())))
  
visited = [[0] * m for _ in range(n)]
move = ((0,1), (1,0), (-1,0), (0, -1))

q = deque([(0, 0)])
visited[0][0] = 1


while q:
  ci, cj = q.popleft()
    
  for mi, mj in move:
    xi, xj = mi+ci, mj+cj
    if 0<=xi<n and 0<=xj<m and visited[xi][xj]== 0 and feild[xi][xj]:
      visited[xi][xj] = visited[ci][cj] + 1
      q.append((xi, xj))

print(visited[n-1][m-1])