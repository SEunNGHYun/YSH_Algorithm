import sys

input = sys.stdin.readline

n = int(input())
member = []
leave = {}

for _ in range(n):
  member.append(list(input().split()))
  
member.sort(key=lambda x:x[0], reverse=True) 

for mem in member :
  if ((mem[0] in leave) and (mem[1] == 'leave') ):
    leave[mem[0]] = -1
  else :
    leave[mem[0]] = 1
    
for name, val in leave.items():
  if(val == 1):
    print(name)
    