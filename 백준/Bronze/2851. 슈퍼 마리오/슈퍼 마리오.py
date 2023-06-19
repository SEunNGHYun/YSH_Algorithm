import sys

input = sys.stdin.readline
total = [0 for _ in range(11)]
check = 100
save = 0
for i in range(10):
  total[i+1] = total[i] + int(input())
  if ((total[i+1] - 100) ** 2) <= (check ** 2) :
    save = i+1
    check = (total[i+1] - 100)

print(total[save])