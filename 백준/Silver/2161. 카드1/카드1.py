import sys 
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque([n for n in range(1, N+1)])

while True:
  print(queue.popleft(), end=' ')
  if len(queue) == 0:
    break
  queue.append(queue.popleft())
print()
  