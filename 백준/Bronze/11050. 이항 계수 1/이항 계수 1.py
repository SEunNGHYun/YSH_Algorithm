import sys

input = sys.stdin.readline

n, k = map(int, input().split())

def fact(num):
    if num < 1:
        return 1
    return num * fact(num-1)

if k == 0:
    print(1)
else:
    print(fact(n) // (fact(k) * fact(n - k)))
