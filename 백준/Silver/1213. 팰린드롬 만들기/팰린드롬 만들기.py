import sys 

input = sys.stdin.readline

S = input().strip()
S = sorted(S)
first = ''
last = ''
check = True
obj = {}

for s in S :
  if (s in obj):
    obj[s] += 1
  else:
    obj[s] = 1
    
for key, val in obj.items():
  if (val > 1):
    while (obj[key] > 1):
      first += key
      obj[key] -= 2

last = first[::-1]

for key, val in obj.items():
  if (val == 1) and check :
    first += key
    check = False
  elif (val == 1) and (check == False) :
    first = ''    

if (len(first) > 0) :
  print(first + last)
else:
  print("I'm Sorry Hansoo")
