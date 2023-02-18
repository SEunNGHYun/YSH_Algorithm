import sys

input = sys.stdin.readline

N, M = map(int, input().split())
check_str = []
correct_str = {}
count = 0

for _ in range(N):
    correct_str[input()] = 0

for _ in range(M):
    check_str.append(input())


for i in range(M):
    if check_str[i] in correct_str:
        count = count + 1

print(count)
