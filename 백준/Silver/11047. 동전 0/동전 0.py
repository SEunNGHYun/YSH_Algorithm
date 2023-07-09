import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cost_li = []

for _ in range(n):
  cost = int(input())
  if (cost <= k):
    cost_li.append(cost)
    
cost_li = reversed(cost_li)
count = 0

for cost in cost_li:
  if (k - cost) >= 0:
    m = k // cost
    k = k - (cost * m)
    count += m
print(count)
    
    