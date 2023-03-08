import sys

input = sys.stdin.readline

n = int(input())

kg_3 = kg_5 = 0

check = n // 5
com = 1


if n % 5 == 0:
    kg_3 = 0
    kg_5 = n // 5
else:
    if n % 3 == 0:
        kg_3 = n // 3
        kg_5 = 0

    i = 0
    while True:
        i += 1
        if (n-(5 * i)) <= 0:
            break
        if (n-(5 * i)) % 3 == 0:
            kg_5 = i
            kg_3 = (n-(5 * i)) // 3

if kg_5 == 0 and kg_3 == 0:
    print(-1)
else:
    print(kg_5 + kg_3)
