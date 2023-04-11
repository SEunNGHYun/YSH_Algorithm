import sys

input = sys.stdin.readline

s = input().strip()


def rev(re_str):
    for i in range(len(re_str)):
        print(re_str.pop(), end='')
    return re_str


check = False
re_str = []
leng = len(s)
for i in range(leng):
    if s[i] == '<':
        if len(re_str) > 0:
            re_str = rev(re_str)
        check = True
    elif s[i] == '>':
        check = False
        re_str = []
        print(s[i], end='')
    elif s[i] == ' ' and check == False:
        if len(re_str) > 0:
            re_str = rev(re_str)
        re_str = []
        print(' ', end='')
    elif i == leng-1:
        if len(re_str) > 0:
            re_str.append(s[i])
            re_str = rev(re_str)
        re_str = []
    else:
        re_str.append(s[i])
    if check == True:
        print(s[i], end='')
