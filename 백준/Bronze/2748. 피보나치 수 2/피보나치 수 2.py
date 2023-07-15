import sys

input = sys.stdin.readline

n = int(input())
fibo = [0, 1] + [0 for _ in range(n-1)]

for i in range(2, n+1):
  fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])