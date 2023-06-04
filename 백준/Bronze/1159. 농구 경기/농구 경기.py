import sys
input = sys.stdin.readline

names = {}
result = []
n = int(input())

for _ in range(n):
    name = input().rstrip()
    if name[0] in names:
        names[name[0]] += 1
    else:
        names[name[0]] = 1

for n, val in names.items():
    if val >= 5:
        result.append(n)

result.sort()

if result == []:
    print('PREDAJA')
else:
    print(''.join(result))