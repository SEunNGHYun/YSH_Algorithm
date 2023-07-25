import sys
import copy
from collections import deque

input = sys.stdin.readline
land = []
high = 0
n = int(input())
visited_copy = [[False] * n for _ in range(n)]

for _ in range(n):
  l = list(map(int, input().split()))
  high = max(max(l), high)
  land.append(l)
  
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
cnt = 0
result = []  
  
for num in range(1, high+1):
  visited = copy.deepcopy(visited_copy)
  cnt = 0
  for i in range(n):
    for j in range(n):
      if (not visited[i][j] and land[i][j] > num):
        q = deque([(i, j)])
        visited[i][j] = True
        cnt += 1

        while q:
          xi, xj = q.popleft()
          for mi, mj in move:
            ci, cj = xi + mi, xj + mj
            if (0<=ci<n) and (0<=cj<n):
              if (not visited[ci][cj]) and (land[ci][cj] > num):
                visited[ci][cj] = True
                q.append((ci, cj))                
  if cnt == 0:
    cnt = 1
  result.append(cnt)

print(max(result))