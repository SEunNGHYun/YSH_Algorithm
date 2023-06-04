import sys
input = sys.stdin.readline
feild = []
white = 0
r = 0
for _ in range(8):

    feild.append(input().rstrip())


for i in range(8):
    if i % 2 == 0:
        r = 0
    else:
        r = 1
    for j in range(r, len(feild[i]), 2):
        if feild[i][j] == 'F':
            white += 1

print(white)
