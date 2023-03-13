import sys

input = sys.stdin.readline

s_char_li = list(input().strip())
s_len = len(s_char_li)
s_li = []

for i in range(s_len):
    s_li.append(''.join(s_char_li[i: s_len]))
s_li.sort()

for s in s_li:
    print(s)
