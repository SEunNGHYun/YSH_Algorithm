import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))

count = 0
i = 0
j = 1
total = 0

while j <= n:
  total = sum(n_li[i : j])
  if total == m :
    count += 1
    j += 1
  elif total < m :
    j += 1
  else :
    i += 1
print(count)