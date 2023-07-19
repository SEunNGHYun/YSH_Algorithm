import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)
n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
count = 1
for _ in range(m):
  n1, n2 = map(int,input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)
  
for nodes in graph: # 오름차순 탐색을 위한 정렬
    nodes.sort()
    
def dfs(s):
  global count
  visited[s] = count
  for i in graph[s]:
    if (not visited[i]):
      count += 1
      dfs(i)

dfs(v)

for i in range(1, n+1):
  print(visited[i])