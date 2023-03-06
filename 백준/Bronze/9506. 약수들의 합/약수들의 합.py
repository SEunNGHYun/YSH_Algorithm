import sys

input = sys.stdin.readline
str_list = []
for _ in range(5):
    s_li = input().strip()
    str_list.append(s_li)

for i in range(15):
    for j in range(5):
        if i < len(str_list[j]):
            print(str_list[j][i], end='')
print()
