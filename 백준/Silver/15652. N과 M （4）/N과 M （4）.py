import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = []
st = set()


def back(s):
    global n, m, li

    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(s, n+1):
        li.append(i)
        back(i)
        li.pop()


back(1)
