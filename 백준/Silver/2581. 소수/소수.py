import sys

input = sys.stdin.readline

m = int(input())
n = int(input())

primes = []
sum_val = 0

if m == 1:
    m = 2


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


while m <= n:
    if isPrime(m):
        sum_val += m
        primes.append(m)
    m += 1

if sum_val == 0:
    print(-1)
else:
    print(sum_val)
    print(min(primes))
