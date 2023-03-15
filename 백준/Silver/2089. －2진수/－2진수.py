import sys

input = sys.stdin.readline

n = int(input())
result = []

if n == 0:
    print(0)
else:
    while n != 0:
        if n % (-2) != 0:
            result.append(1)
            n = (n // -2) + 1
        else:
            result.append(0)
            n = (n // -2)

    for n in result[::-1]:
        print(n, end='')
    print()
