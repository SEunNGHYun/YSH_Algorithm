import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    str = list(input().split())
    for i in range(len(str)):
        print(str[i][::-1], end=' ')
    print()
