import sys

input = sys.stdin.readline
s = input()
s_li = list(s.strip().split('.'))
wrong = False

for i in range(len(s_li)):
  leng = len(s_li[i])
  if (leng % 2 == 0):
    x = ''
    while (leng > 0) :
      if (leng >= 4):
        x += 'AAAA'
        leng -= 4
      else :
        x += 'BB'
        leng -= 2
    s_li[i] = x
  else:
    wrong = True
    break 
  
  
if wrong:
  print(-1)
else:
  for i in range((len(s_li) - 1)):
    print(s_li[i], end='')
    if (s_li[i+1] != '.'):
      print('.', end='')
  print(s_li[-1])