import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

val = x
# 0, ~ 기준
if val > y:
    val = y
# ~, 0 기준
if val > w-x:
    val = w - x
# w, 0 기준
if val > h - y:
    val = h - y
# 0, h 기준
print(val)
