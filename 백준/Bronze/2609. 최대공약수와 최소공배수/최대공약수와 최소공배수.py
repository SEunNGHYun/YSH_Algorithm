import sys

input = sys.stdin.readline


num1, num2 = map(int, input().split())
gcd = lcm = 1


def GCD(large, small):  # 최대 공배수
    if large % small == 0:
        return small
    else:
        return GCD(small, large % small)

def LCM(n1, n2):
    global gcd
    return (n1*n2) // gcd


if num1 > num2:
    gcd = GCD(num1, num2)
else:
    gcd = GCD(num2, num1)


lcm = LCM(num1, num2)

print(gcd)
print(lcm)
