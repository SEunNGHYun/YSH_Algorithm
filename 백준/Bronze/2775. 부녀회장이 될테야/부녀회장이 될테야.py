import sys

input = sys.stdin.readline

t = int(input())
apt = [[n for n in range(1, 16)]]

if (t > 1):
    for i in range(1, 15):
        apt_li = [1 for _ in range(1, 16)]
        for j in range(1, 15):
            apt_li[j] = apt_li[j-1] + apt[i-1][j]
        apt.append(apt_li)

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])
