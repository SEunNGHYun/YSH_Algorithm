import sys

input = sys.stdin.readline

n = int(input())
total = (2 * n) - 1

half = total // 2

for i in range(n):
    for j in range(total):
        if (half-i) <= j and j <= (half+i):
            print('*', end='')
        elif j < (half-i):
            print(' ', end='')
    print()

for i in range(1, n):
    for j in range(total):
        if (i) <= j and j < (total-i):
            print('*', end='')
        elif j < i:
            print(' ', end='')
    print()
