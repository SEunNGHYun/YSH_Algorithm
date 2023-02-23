import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pocket_mon_key_num = {}
pocket_mon_key_str = {}
problems = []

for num in range(1, n+1):
    pocket_mon = input().strip()
    pocket_mon_key_num[str(num)] = pocket_mon
    pocket_mon_key_str[pocket_mon] = str(num)

for _ in range(m):
    problem = input().strip()
    if problem in pocket_mon_key_num:
        print(pocket_mon_key_num[problem])
    else:
        print(int(pocket_mon_key_str[problem]))
