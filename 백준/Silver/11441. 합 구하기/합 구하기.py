import sys

input = sys.stdin.readline
n = int(input())

n_li = list(map(int, input().split()))
n_li_sum = [0 for _ in range(n + 1)]

m = int(input())

for i in range(n):
  n_li_sum[i+1] = n_li_sum[i] + n_li[i]

for _ in range(m):
  i, j = map(int, input().split())
  print(n_li_sum[j] - n_li_sum[i-1])