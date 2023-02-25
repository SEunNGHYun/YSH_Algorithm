import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dict = {}
    count = 1
    for _ in range(n):
        clo, clo_type = input().split()
        if clo_type in dict:
            dict[clo_type] += 1
        else:
            dict[clo_type] = 1

    for value in dict.values():
        count *= value + 1
    print(count - 1)