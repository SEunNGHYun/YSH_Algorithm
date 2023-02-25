import sys

input = sys.stdin.readline

n = int(input())
dp_fact = [1, 1, 2, 6]  # 0! ~ 3!

for i in range(4, n+1):
    dp_fact.append(dp_fact[i-1] * i)

str_num = str(dp_fact[n])
zero_count = 0

for i in range(len(str_num)-1, -1, -1):
    if str_num[i] == '0':
        zero_count += 1
    else:
        break

print(zero_count)
