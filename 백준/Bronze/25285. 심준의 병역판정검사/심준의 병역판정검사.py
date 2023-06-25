import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
  cm, kg = map(float, input().split())
  if cm < 159 : 
    if cm < 140.1:
      print(6)
    elif 140.1 <= cm and cm < 146 :
      print(5)
    else: 
      print(4)
  else:
    bmi = (kg / (round((cm / 100), 3) ** 2))
    if (cm >= 159 and cm < 161)  :
      if (bmi >= 16 and bmi < 35):
        print(3)
      else:
        print(4) 
    elif (cm >= 161 and cm < 204):
      
      if (16 <= bmi and bmi < 18.5) or (30 <= bmi and bmi < 35):
        print(3)
      elif (18.5 <= bmi and bmi < 20) or (25 <= bmi and bmi < 30):
        print(2)
      elif (20 <= bmi and bmi < 25):
        print(1)
      else:
        print(4) 
    else :
      print(4)