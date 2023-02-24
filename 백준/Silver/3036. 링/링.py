import sys

input = sys.stdin.readline

n = int(input())
n_li = list(map(int, input().split()))


def GCD(large, small):  # 최대 공배수
    if large % small == 0:
        return small
    else:
        return GCD(small, large % small)


for i in range(1, n):
    gcd = 1
    if n_li[0] > n_li[i]:
        gcd = GCD(n_li[0], n_li[i])
    else:
        gcd = GCD(n_li[i], n_li[0])

    print(n_li[0] // gcd, end='/')
    print(n_li[i] // gcd)
