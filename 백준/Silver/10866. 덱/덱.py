import sys

input = sys.stdin.readline

n = int(input())
li = []


def stack(action):
    global li

    if action[0] == 'push_back':
        li.append(int(action[1]))
    elif action[0] == 'push_front':
        li = [int(action[1])] + li
    elif action[0] == 'pop_back':
        if len(li) == 0:
            print(-1)
        else:
            pop_val = li[len(li)-1]
            li = li[:len(li)-1]
            print(pop_val)
    elif action[0] == 'pop_front':
        if len(li) == 0:
            print(-1)
        else:
            pop_val = li[0]
            li = li[1:]
            print(pop_val)
    elif action[0] == 'front':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    elif action[0] == 'back':
        if len(li) == 0:
            print(-1)
        else:
            print(li[len(li)-1])
    elif action[0] == 'size':
        print(len(li))
    elif action[0] == 'empty':
        if len(li) == 0:
            print(1)
        else:
            print(0)


for _ in range(n):
    str = list(input().split())
    stack(str)
