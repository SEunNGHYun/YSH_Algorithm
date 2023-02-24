import sys

input = sys.stdin.readline

n = int(input())
num_n_dict = {}
num_n_li = list(map(int, input().split()))
m = int(input())
num_m_li = list(map(int, input().split()))

for num in num_n_li:
    if num in num_n_dict:
        num_n_dict[num] += 1
    else:
        num_n_dict[num] = 1


for num in num_m_li:
    if num in num_n_dict:
        print(num_n_dict[num], end=' ')
    else:
        print(0, end=' ')
