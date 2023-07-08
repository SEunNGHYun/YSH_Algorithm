import sys
input = sys.stdin.readline

n = int(input())
n_li = []
result = 0

for i in range(n):
  n_li.append(int(input()))

n_li.sort()

for i in range(n):
  mi = n_li[i]
  if ((mi * (n-i)) > result):
    result = (mi * (n-i))
    
print(result)