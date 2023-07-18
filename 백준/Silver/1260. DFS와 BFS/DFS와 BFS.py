import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n + 1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
  n1, n2 = map(int, input().split())
  graph[n1][n2] = graph[n2][n1] = True
  
def dfs(s):
  visited_dfs[s] = True
  print(s, end= ' ')
  for i in range(1, n+1):
    if (visited_dfs[i] == False and graph[s][i] == True) :
      dfs(i)
dfs(v)
print()

def bfs(s):
  q = deque([s])
  visited_bfs[s] = True
  
  while q:
    x = q.popleft()
    print(x, end = ' ')
    for i in range(1, n+1):
      if (visited_bfs[i] == False and graph[x][i] == True):
        q.append(i)
        visited_bfs[i] = True

bfs(v)
print()