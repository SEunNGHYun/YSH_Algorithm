import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
n_li = deque([i for i in range(1, n+1)])

while n > 1:
  n -= 1
  n_li.popleft()
  n_li.append(n_li.popleft())
  
  
print(n_li[0])