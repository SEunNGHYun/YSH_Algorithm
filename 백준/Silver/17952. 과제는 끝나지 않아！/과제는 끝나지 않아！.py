import sys

input = sys.stdin.readline

n = int(input())
work_li = []
score = 0

for _ in range(n):
  work = input()
  working = []
  if work_li :
    working = work_li[-1]
  
  if work[0] == '1':
    working = list(map(int, work[2:].split()))
    work_li.append(working)
  
  if working :
    working[1] = working[1] - 1
  
  if working and working[1] == 0:
    score += working[0]
    work_li.pop()

print(score)
