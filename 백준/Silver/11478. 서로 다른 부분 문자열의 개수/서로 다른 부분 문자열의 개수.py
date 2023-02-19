import sys

input = sys.stdin.readline

str = input().strip()
leng = len(str)

totalSet = set([str])
# 문자열 전체 넣어주기

for i in range(1, leng):
    first = 0
    last = i
    while last < leng + 1:
        totalSet.add(str[first:last])  # set에 인덱싱한 문자열 추가
        # first와 last 다음 인데스로 넘어가기
        first = first + 1
        last = last + 1

print(len(totalSet))
