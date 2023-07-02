import sys 
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
li_n = [n for n in range(1, N+1)]
k = K
result_n = []
while len(li_n) > 0 :
  n = li_n.pop(0)
  k -= 1
  if k == 0 :
    k = K
    result_n.append(n)
  else:
    li_n.append(n)  
print("<", end='')
print(', '.join(map(str, result_n)), end='')
print('>')