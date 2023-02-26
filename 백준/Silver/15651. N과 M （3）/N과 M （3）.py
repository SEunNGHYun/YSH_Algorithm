import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = []
st = set()


def back():
    global n, m, li

    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(1, n+1):
        li.append(i)
        back()
        li.pop()


back()
