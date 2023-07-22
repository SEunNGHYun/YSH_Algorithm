import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
feild = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
  feild.append(list(map(int, input().strip())))
result = []
move = ((-1,0),(1,0),(0,-1),(0,1))
# x, y 좌표 기준 (x, y) (좌, 우, 하, 상)

def bfs (si, sj):
  q = deque([(si, sj)])
  visited[si][sj] = 1
  cnt = 1

  while q : 
    ci, cj = q.popleft()
    for di, dj in move:
      ni, nj = ci+di, cj+dj
      if (0<=ni<n) and (0<=nj<n) and visited[ni][nj] == 0 and feild[ni][nj] == 1:
        q.append((ni, nj))
        visited[ni][nj] = 1
        cnt += 1
  return cnt

for i in range(n):
  for j in range(n):
    if feild[i][j] == 1 and visited[i][j] == 0 :
      result.append(bfs(i, j))
      
print(len(result))
result.sort()
for dangi in result:
  print(dangi)