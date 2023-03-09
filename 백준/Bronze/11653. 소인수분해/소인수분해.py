import sys

input = sys.stdin.readline


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


n = int(input())

num = 2

if n != 1:
    while True:
        if isPrime(n):
            print(n)
            break

        if isPrime(num):
            if n % num == 0:
                n = n // num
                print(num)
            else:
                num += 1
        else:
            num += 1
