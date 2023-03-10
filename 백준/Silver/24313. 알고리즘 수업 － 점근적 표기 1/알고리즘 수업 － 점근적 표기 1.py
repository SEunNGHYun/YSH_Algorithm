import sys

input = sys.stdin.readline

a1, a2 = map(int, input().split())

c = int(input())

o = int(input())

check = True

for n in range(o, 101):
    if ((a1 * n) + a2) > (c * n):
        check = False
        break

if check == False:
    print(0)
else:
    print(1)
