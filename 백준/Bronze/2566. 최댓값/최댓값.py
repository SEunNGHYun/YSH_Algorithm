import sys

input = sys.stdin.readline

# x,y는 색종이의 시작좌표
# 시작 좌표부터 +10

row, col = 1, 1
maxVal_total = 0

for i in range(1, 10):
    li = list(map(int, input().split()))
    maxVal_in_li = max(li)
    if maxVal_total < maxVal_in_li:
        row = i
        col = li.index(maxVal_in_li) + 1
        maxVal_total = maxVal_in_li


print(maxVal_total)
print(row, end=' ')
print(col)
