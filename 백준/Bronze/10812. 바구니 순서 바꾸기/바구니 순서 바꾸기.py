import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = [i for i in range(1, n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    head = li[:i-1]
    tail = li[j:]
    body = li[k-1:j] + li[i-1:k-1]
    li = head + body + tail


print(' '.join(map(str, li)))
