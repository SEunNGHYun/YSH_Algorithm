import sys

n = int(input())
s = input().strip()
val = []

for _ in range(n):
    val.append(int(input()))

alphabat = {}
index1 = 0
for i in range(len(s)):
    ascii_s = ord(s[i])
    if 65 <= ascii_s and ascii_s <= 90:
        if s[i] not in alphabat:
            alphabat[s[i]] = val[index1]
            index1 += 1
val_li = []
index2 = 0

for i in range(len(s)):
    if s[i] in alphabat:
        val_li.append(alphabat[s[i]])
    else:
        last = val_li.pop()
        first = val_li.pop()
        value = 0
        if s[i] == '-':
            value = first - last
        elif s[i] == '*':
            value = first * last
        elif s[i] == '/':
            value = first / last
        elif s[i] == '+':
            value = first + last
        val_li.append(value)
print('{:.2f}'.format(val_li[0]))
