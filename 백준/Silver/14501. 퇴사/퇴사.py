import sys

input = sys.stdin.readline

n = int(input())
works = []
ach = 0

for i in range(n):
  w = list(map(int, input().split()))
  works.append(w)

dp_work = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
  day, pay = works[i][0], works[i][1]
  if (day + i) > n : # 끝냈을 때가 퇴사날 지났을 때
    dp_work[i] = dp_work[i+1]
    # 이전의 수당 가져오가
  else:
    dp_work[i] = max(dp_work[i+1], dp_work[day + i] + pay)
    # 이전의 수당과 (현재 수당과 끝났을 때 받는 수당을 더했을 때 ) 비교
print(dp_work[0])