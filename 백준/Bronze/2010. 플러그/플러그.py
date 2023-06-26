import sys

input = sys.stdin.readline

n = int(input())
result = [0 for _ in range(n+1)]

for i in range(1, n+1):
  result[i] = int(input())
  if i > 1 :
    result[i-1] -= 1

print(sum(result))