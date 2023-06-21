import sys

input = sys.stdin.readline
n_dict = {}
n = int(input())
n_li = list(map(int, input().split()))
n_dict = {}
m = int(input())
m_li = list(map(int, input().split()))

for i in range(n):
  n_dict[n_li[i]] = 1
for i in range(m):
  if m_li[i] in n_dict:
    print(n_dict[m_li[i]])
  else:
    print(0)
