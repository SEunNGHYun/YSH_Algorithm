import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = [i for i in range(1, n+1)]
result = []
while len(li) >= k:
    result.append(li[k-1])

    li = li[k:] + li[0: k-1]

for i in range(len(li)):
    index = 0
    for _ in range(k-1):
        if index == len(li)-1:
            index = 0
        else:
            index += 1

    result.append(li[index])
    li = li[index+1:] + li[0: index]


result = result + li

print('<'+', '.join(map(str, result)) + '>')
