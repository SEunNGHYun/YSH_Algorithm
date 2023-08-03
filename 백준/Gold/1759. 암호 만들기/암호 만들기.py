import sys

input = sys.stdin.readline

l, c = map(int, input().split())
w = list(input().strip().split())
m = ["a", "e", "i", "o", "u"]
answer = []
w.sort()

def back(cnt, idx):
  
  if cnt == l:
    vo, co = 0, 0
    
    for i in range(l):
      if answer[i] in m:
        vo += 1
      else:
        co += 1
    
    if vo >= 1 and co >= 2:
      print(''.join(answer))
      
      return 
  
  for i in range(idx, c):
    answer.append(w[i])
    back(cnt+1, i+1)
    answer.pop()

back(0, 0)