import sys

input = sys.stdin.readline

n = input().strip()
set_count = 1
number_set = { str(i):1 for i in range(10)}

for i in range(len(n)):
  if number_set[n[i]] > 0:
    number_set[n[i]] -= 1
  elif  number_set[n[i]] == 0 and (n[i] == '9' or n[i] == '6') : 
    if n[i] == '9' and number_set["6"] > 0:
        number_set["6"] -= 1
    elif n[i] == '6' and number_set["9"] > 0:
        number_set["9"] -= 1
    else:
      set_count += 1
      for k, v in number_set.items():
        if k != n[i]:
          number_set[k] = v + 1
  else:
    set_count += 1
    for k, v in number_set.items():
      if k != n[i]:
        number_set[k] = v + 1
print(set_count)