import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    S = input().rstrip()
    s_li_l = []
    s_li_r = []
    for i in range(len(S)):
        if s_li_l and S[i] == '<':
            s = s_li_l.pop()
            s_li_r.append(s)
        elif s_li_r and S[i] == ">":
            s = s_li_r.pop()
            s_li_l.append(s)
        elif s_li_l and S[i] == "-":
            s_li_l.pop()
        elif S[i] != '>' and S[i] != '<' and S[i] != "-":
            s_li_l.append(S[i])

    s_li_l += reversed(s_li_r)
    print(''.join(s_li_l))
