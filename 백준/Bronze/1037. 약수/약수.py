import sys

input = sys.stdin.readline

n_divisor_count = int(input())
n_divisor_li = list(map(int, input().split()))

n_divisor_min = min(n_divisor_li)
n_divisor_max = max(n_divisor_li)

print(n_divisor_max * n_divisor_min)
