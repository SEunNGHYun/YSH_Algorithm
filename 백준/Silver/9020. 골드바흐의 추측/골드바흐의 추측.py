import sys


def isPrime(val):
    count = 0
    num = 2

    while num * num <= val:
        if (val % num) == 0:
            count += 1
        num += 1

    if count == 0:
        return True
    else:
        return False


input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    half = left = num//2

    for right in range(half, num):
        if isPrime(left) and isPrime(right):
            print(left, right)
            break
        left -= 1
