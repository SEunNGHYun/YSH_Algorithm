import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(1+n)]

for _ in range(m):
  n1,n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)
  
for i in range(1, n+1):
  graph[i] = reversed(sorted(graph[i]))

turn = 1
def dfs(s):
  global turn 
  visited[s] = turn
  turn += 1

  for i in graph[s]:
    if not visited[i]:
      dfs(i)
      
dfs(v)

for i in range(1, n+1):
  print(visited[i])
