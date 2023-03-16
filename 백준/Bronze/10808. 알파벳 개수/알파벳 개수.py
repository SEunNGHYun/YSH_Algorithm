import sys

input = sys.stdin.readline

s = input().strip()
s_li = [0 for i in range(26)]

for i in range(len(s)):
    asc2 = ord(s[i])
    if 97 <= asc2 and asc2 <= 122:
        s_li[asc2-97] += 1
print(' '.join(map(str, s_li)))
