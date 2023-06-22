import sys

input = sys.stdin.readline
check = [1, 2, 3, 4, 5, 4, 3, 2]
f = int(input())
use = int(input())
result = 0

if (use < 3) and (f != 5 and f != 1):
  for i in range(8) :
    if (check[i] == f) and (use == 0):
      break
    elif (check[i] == f):
      use -= 1
    result += 1
else:
  if f == 1 or f == 5 :
    result = (use) * 8
    use = 0
    for i in range(8):
      if (check[i] == f) and (use == 0):
        break
      result += 1
  else :
    result = (use // 2) * 8
    use = (use % 2)
    for i in range(8):
      if (check[i] == f) and (use == 0):
        break
      elif (check[i] == f):
        use -= 1
      result += 1

print(result)