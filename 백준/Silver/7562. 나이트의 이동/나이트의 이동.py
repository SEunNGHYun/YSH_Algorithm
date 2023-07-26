import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
move = ((-2,-1),(-1,-2),(-2, 1),(-1, 2),(2, -1),(1, -2),(1, 2),(2, 1))
for _ in range(n):
  l = int(input())
  s = tuple(map(int, input().split()))
  e = tuple(map(int, input().split()))
  visited = [[0] * l for _ in range(l)]
  
  q = deque([s])
  
  while q: 
    xi, xj = q.popleft()
    
    for mi, mj in move:
      ci, cj = (mi + xi), (mj + xj)
      if 0<=ci<l and 0<=cj<l:
        if (not visited[ci][cj]):
          q.append((ci, cj))
          visited[ci][cj] = visited[xi][xj] + 1
  visited[s[0]][s[1]] = 0      
  print(visited[e[0]][e[1]])