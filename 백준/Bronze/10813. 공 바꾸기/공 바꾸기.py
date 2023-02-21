import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bucket = {}

for i in range(1, N+1):
    bucket[i] = i


for _ in range(M):
    swap_a, swap_b = map(int, input().split())
    save = bucket[swap_a]
    bucket[swap_a] = bucket[swap_b]
    bucket[swap_b] = save

for val in bucket.values():
    print(val, end=' ')
