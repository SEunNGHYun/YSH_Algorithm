import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())

total_time = 0

while True:
  if x == 0 and y == 0 :
    total_time += 0
    break
  elif x == 0 or y == 0 :
    if x == 0:
      if w < s : # 직선 시간이 빠를 때
        total_time += (y * w) # y길이 만큼만 직선 이동.
      else: # 대각선이 빠를 때
        if (y % 2) == 0: 
          total_time += (y * s) # y길이 만큼만 대각선으로 이동
        else : # 대각선으로 이동 하고 나머지는 가로로 이동
          total_time += ((((y // 2) * 2) * s) + w)
      y = 0
    else:
      if w < s : # 직선 시간이 빠를 때
        total_time += (x * w) # x길이 만큼만 직선 이동.
      else: # 대각선이 빠를 때
        if (x % 2) == 0: 
          total_time += (x * s) # x길이 만큼만 대각선으로 이동
        else : # 대각선으로 이동 하고 나머지는 가로로 이동
          total_time += ((((x // 2) * 2) * s) + w)
      x = 0
  else:
    if (2 * w) < s: # 직선이 빠를 때
      total_time += (x * w) + (y * w)
      x, y = 0, 0
    else :
      if x > y:
        total_time += (y * s)
        x -= y
        y = 0
      else :
        total_time += (x * s)
        y -= x
        x = 0      
        
    
    
print(total_time)