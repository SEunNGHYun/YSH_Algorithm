import sys

input = sys.stdin.readline

sosu = [False, False] + [True] * 1000000

for i in range(2, 1000):
    if sosu[i]:
        for j in range(i * 2, 1000000, i):
            sosu[j] = False

while True:
    n = int(input())
    half_n = n // 2
    check = True
    if n < 6:
        break
    for a in range(3, half_n + 1, 2):
        if sosu[a] and sosu[n - a]:
            print("{} = {} + {}".format(n, a, (n-a)))
            check = False
            break
    if check:
        print("Goldbach's conjecture is wrong.")
