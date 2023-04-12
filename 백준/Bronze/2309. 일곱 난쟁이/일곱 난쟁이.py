import sys

input = sys.stdin.readline

li = []

for _ in range(9):
    li.append(int(input()))

li.sort()

found = sum(li) - 100
end = False

for i in range(9):
    for j in range(i+1, 9):
        if li[i] + li[j] == found:
            li[i] = -1
            li[j] = -1
            end = True
            break
    if end == True:
        break

for t in li:
    if t != -1:
        print(t)
