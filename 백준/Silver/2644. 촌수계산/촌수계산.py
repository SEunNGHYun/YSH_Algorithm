import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
p_li = [[] for _ in range(n+1)]
visited = [[0] for _ in range(n+1)]

for _ in range(m):
  i, j = map(int, input().split())
  p_li[i].append(j)
  p_li[j].append(i)
  
q = deque([p1])
visited[p1][0] = 0

while q:
  x = q.popleft()
  
  for p in p_li[x]:
    if not visited[p][0]:
      visited[p][0] = visited[x][0] + 1
      q.append(p)
    
      
if visited[p2][0] == 0:
  print(-1)
else:
  print(visited[p2][0])
