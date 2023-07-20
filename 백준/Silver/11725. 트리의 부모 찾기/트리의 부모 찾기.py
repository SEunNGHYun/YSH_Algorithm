import sys

input = sys.stdin.readline

n = int(input())
graph = dict()
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
  n1, n2 = map(int, input().split())
  if (n1 in graph):
    graph[n1].append(n2)
  else:
    graph[n1] = [n2]

  if (n2 in graph):
    graph[n2].append(n1)
  else:
    graph[n2] = [n1]
    
stack = [1]

while stack:
  p = stack.pop()
  for i in graph[p]:
    if not visited[i]:
      visited[i] = p
      stack.append(i)
      

for i in range(2, n+1):
  print(visited[i])