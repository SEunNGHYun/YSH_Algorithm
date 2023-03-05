import sys

input = sys.stdin.readline

total = 0
total_score = 0

for i in range(20):
    name, score, clas = map(str, input().split())

    score = float(score)
    if clas != 'P':
        total_score += score

    if clas == 'A+':
        total += (score * 4.5)
    elif clas == 'A0':
        total += (score * 4.0)
    elif clas == 'B+':
        total += (score * 3.5)
    elif clas == 'B0':
        total += (score * 3.0)
    elif clas == 'C+':
        total += (score * 2.5)
    elif clas == 'C0':
        total += (score * 2.0)
    elif clas == 'D+':
        total += (score * 1.5)
    elif clas == 'D0':
        total += (score * 1.0)
    else:
        total += (score * 0.0)
        # p와 f
print('%.6f' % (total / total_score))
