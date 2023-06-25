import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

if (a * b) == c:
  print('{}*{}={}'.format(a,b,c))
elif (a / b) == c:
  print('{}/{}={}'.format(a,b,c))
elif (a - b) == c:
  print('{}-{}={}'.format(a,b,c))
elif (a + b) == c:
  print('{}+{}={}'.format(a,b,c))
else :
  if (b * c) == a:
    print('{}={}*{}'.format(a,b,c))
  elif (b / c) == a:
    print('{}={}/{}'.format(a,b,c))
  elif (b - c) == a:
    print('{}={}-{}'.format(a,b,c))
  elif (b + c) == a:
    print('{}={}+{}'.format(a,b,c))
