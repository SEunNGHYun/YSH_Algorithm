import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bucket = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        bucket[index] = k


for boll in bucket:
    print(boll, end=' ')
