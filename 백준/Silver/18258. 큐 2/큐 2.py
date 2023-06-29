import sys 
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
  method = input().strip()
  if method[0:2] == 'pu':
    method, val = map(str, method.split())
    queue.append(int(val))
  else :
    if method == 'pop':
      if len(queue) > 0:
        print(queue.popleft())
      else:
        print(-1)
    elif method == 'size':
      print(len(queue))
    elif method == 'empty':
      if len(queue) > 0:
        print(0)
      else:
        print(1)
    elif method == 'front':
      if len(queue) > 0:
        print(queue[0])
      else:
        print(-1)
    elif method == 'back':
      if len(queue) > 0:
        print(queue[-1])
      else:
        print(-1)
      