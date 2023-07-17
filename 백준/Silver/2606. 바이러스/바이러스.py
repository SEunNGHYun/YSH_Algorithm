import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
com = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for i in range(m):
  com1, com2 = map(int, input().split())
  com[com1].append(com2)
  com[com2].append(com1)

count = 0

def dfs(w):
  global count
  visited[w] = True
  for n in com[w]:
    if not visited[n]:
      count += 1
      dfs(n)
dfs(1)

print(count)