import sys

input = sys.stdin.readline

tr = []
for _ in range(3):
    d = int(input())
    tr.append(d)

if sum(tr) == 180:
    check = False
    pre_d = tr[0]
    if tr[0] == tr[1] or tr[2] == tr[1] or tr[0] == tr[2]:
        check = True
    if check:
        if pre_d == 60:
            print('Equilateral')
        else:
            print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
