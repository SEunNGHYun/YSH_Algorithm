import sys

input = sys.stdin.readline

t = int(input())
result = []
i = 1
count = 0


def bfs(a):
    global count

    if a == 0:
        count += 1
        return

    if a - 1 >= 0:
        bfs(a-1)
    if a - 2 >= 0:
        bfs(a-2)
    if a - 3 >= 0:
        bfs(a-3)


for _ in range(t):
    n = int(input())
    n_li = []
    count = 0
    for i in range(1, 4):
        bfs(n-i)
    print(count)
