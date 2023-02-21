import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bucket = []

for i in range(1, N+1):
    bucket.append(i)

for _ in range(M):
    swap_a, swap_b = map(int, input().split())
    bucket = bucket[:swap_a-1:] + \
        list(reversed(bucket[swap_a-1: swap_b])) + bucket[swap_b::]

for n in bucket:
    print(n, end=' ')

