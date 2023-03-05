import sys

input = sys.stdin.readline

s = input().strip()
s_len = len(s)
s_len_half = s_len // 2
s_front = ''
s_back = ''

for i in range(s_len_half):
    s_front += s[i]
if s_len % 2 == 0:
    s_len_half -= 1
for i in range(s_len - 1, s_len_half, -1):
    s_back += s[i]

print(1 if s_back == s_front else 0)
