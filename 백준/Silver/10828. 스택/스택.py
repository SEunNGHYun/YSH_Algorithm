import sys

input = sys.stdin.readline

n = int(input())

arr = []


def stack(action):
    global arr
    if action[0] == 'push':
        arr.append(action[1])
    elif action[0] == 'pop':
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)
    elif action[0] == 'size':
        print(len(arr))
    elif action[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif action[0] == 'top':
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)


for _ in range(n):
    action = list(input().split())
    stack(action)
