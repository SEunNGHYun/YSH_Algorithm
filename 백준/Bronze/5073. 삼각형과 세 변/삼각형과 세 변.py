import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

while a != 0 and b != 0 and c != 0:
  li_n = sorted([a,b,c])

  if li_n[2] >= (li_n[1] + li_n[0]) :
    print('Invalid')
  else:
    if a == b and b == c :
        print('Equilateral')
    elif a == b or a == c or c == b :
        print('Isosceles')
    else:
        print('Scalene')

  a, b, c = map(int, input().split())
