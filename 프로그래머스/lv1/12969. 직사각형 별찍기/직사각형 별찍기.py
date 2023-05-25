import sys
input = sys.stdin.readline
m, n = map(int, input().split())

for _ in range(n):
    for _ in range(m):
        print('*', end='')
    print()