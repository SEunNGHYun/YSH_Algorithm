import sys

input = sys.stdin.readline

N, M = map(int, input().split())
notListen = []
notLook = {}
notListen_notLook = []

for _ in range(N):
    notListen.append(input().strip())

for _ in range(M):
    notLook[input().strip()] = 0

for i in range(N):
    if notListen[i] in notLook:
        notListen_notLook.append(notListen[i])

notListen_notLook_count = len(notListen_notLook)
notListen_notLook.sort()

print(notListen_notLook_count)
for i in range(notListen_notLook_count):
    print(notListen_notLook[i])
