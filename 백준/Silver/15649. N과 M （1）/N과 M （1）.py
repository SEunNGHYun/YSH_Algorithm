import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = []

def back():
    global n, m, li

    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(1, n+1):
        if i not in li:
            li.append(i)
            back()
            li.pop()

back()
