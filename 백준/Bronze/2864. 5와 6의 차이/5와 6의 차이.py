import sys

input = sys.stdin.readline

a, b = input().split()

max_b, min_b = '', ''
max_a, min_a = '', ''


for i in range(len(a)):
  if (a[i] == '5'):
    max_a += '6'
    min_a += a[i]
  elif (a[i] == '6'):
    min_a += '5'
    max_a += a[i]
  else:
    max_a += a[i]
    min_a += a[i]
    

for i in range(len(b)):
  if (b[i] == '5'):
    max_b += '6'
    min_b += b[i]
  elif (b[i] == '6'):
    min_b += '5'
    max_b += b[i]
    
  else:
    max_b += b[i]
    min_b += b[i]
    
    
max_b,min_b = int(max_b), int(min_b)
max_a,min_a = int(max_a), int(min_a)


print((min_a + min_b), (max_a + max_b))