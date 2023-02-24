import sys

input = sys.stdin.readline

answer = ['factor', 'multiple', 'neither']
n, m = map(int, input().split())

while n != 0 and m != 0:

    if m % n == 0:
        print(answer[0])
    elif n % m == 0:
        print(answer[1])
    else:
        print(answer[2])

    n, m = map(int, input().split())
