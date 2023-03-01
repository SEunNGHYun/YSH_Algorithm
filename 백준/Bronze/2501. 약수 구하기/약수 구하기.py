import sys

input = sys.stdin.readline


n, k = map(int, input().split())
li = [1]

for num in range(2, n+1):
    if n % num == 0:
        li.append(num)

if k <= len(li):
    print(li[k-1])
else:
    print(0)
