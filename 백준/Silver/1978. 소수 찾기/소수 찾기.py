import sys

input = sys.stdin.readline

n = int(input())
n_li = list(map(int, input().split()))
result = 0

for i in range(n):
    count = 0
    if n_li[i] == 1:
        count += 1
    for num in range(2, n_li[i]):
        if n_li[i] % num == 0:
            count += 1
    if count == 0:
        result += 1

print(result)
