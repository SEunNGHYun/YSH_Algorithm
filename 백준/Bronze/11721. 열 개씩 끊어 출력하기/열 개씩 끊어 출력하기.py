import sys 

input = sys.stdin.readline

s = input().strip()
i, count = 0, 1

endpoint = True
while (i < len(s)):
  print(s[i], end='')
  endpoint = True
  if (count == 10):
    print('')
    count = 0
    endpoint = False
  i += 1
  count += 1
if (endpoint == True):
    print('')
