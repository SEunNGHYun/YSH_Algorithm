import sys

input = sys.stdin.readline

n = int(input())
result = [-1 for _ in range(n-1)] + [0]

for i in range(n):
  result[i] += int(input())
  
print(sum(result))