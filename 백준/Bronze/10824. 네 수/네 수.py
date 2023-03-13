import sys

input = sys.stdin.readline

A, B, C, D = map(str, input().split())

a_b = int(A+B)
c_d = int(C+D)

print(a_b + c_d)
