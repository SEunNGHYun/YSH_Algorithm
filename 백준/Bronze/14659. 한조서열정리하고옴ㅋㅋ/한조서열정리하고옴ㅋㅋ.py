import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
i = 0
cnt = 0
result = 0

while (i + cnt) < (n - 1):
  cnt = 0
  for j in range(i+1, n):
    if m[i] < m[j]:
      i = j
      break
    else :  
      cnt += 1
  if result < cnt :
    result = cnt
print(result)