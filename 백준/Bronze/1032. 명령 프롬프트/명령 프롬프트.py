import sys

input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    li.append(input().strip())

len_s = len(li[0])
li2 = ['' for _ in range(len_s)]

for s in li:
    for i in range(len_s):
        if li2[i] == '':
            li2[i] = s[i]
        elif li2[i] != s[i]:
            li2[i] = '?'

print(''.join(map(str, li2)))
