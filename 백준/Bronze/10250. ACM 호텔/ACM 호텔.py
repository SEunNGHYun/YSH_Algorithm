import sys

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    head = n % h
    tail = n // h

    if head == 0:
        print(((h * 100) + (tail)))
    else:
        print(((head * 100) + (tail+1)))
