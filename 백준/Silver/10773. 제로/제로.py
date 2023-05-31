import sys

input = sys.stdin.readline

k = int(input())
arr = []
result = 0

for _ in range(k):
    n = int(input())
    if n == 0:
        val = arr.pop()
        result -= val
    else:
        arr.append(n)
        result += n

print(result)
