import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    str = input().strip()
    str_li = []
    answer = 'YES'

    for s in str:
        if s == '(':
            str_li.append(s)
        elif s == ')':
            if len(str_li) > 0:
                str_li.pop()
            else:
                answer = 'NO'
                break
    if len(str_li) > 0:
        answer = 'NO'

    print(answer)
