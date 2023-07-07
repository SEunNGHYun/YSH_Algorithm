import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()
p_sum = [0 for _ in range(n+1)]
for i in range(1, n+1):
  p_sum[i] = p_sum[i-1] + p[i-1]
  
print(sum(p_sum))