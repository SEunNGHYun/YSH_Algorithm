import sys

input = sys.stdin.readline

n = int(input())


def GCD(large, small):  # 최대 공배수
    if large % small == 0:
        return small
    else:
        return GCD(small, large % small)


for _ in range(n):
    num1, num2 = map(int, input().split())
    gcd = 0
    if num1 > num2:
        gcd = GCD(num1, num2)
    else:
        gcd = GCD(num2, num1)

    def LCM(n1, n2):
        global gcd
        return (n1*n2) // gcd

    lcm = LCM(num1, num2)
    print(lcm)
