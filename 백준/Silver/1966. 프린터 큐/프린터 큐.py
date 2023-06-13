import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  n, m = map(int, input().split())
  works = list(map(int, input().split()))
  works_li = [{ "id" : i, "val" : works[i]} for i in range(n)]
  turn = 0
  
  while True:
    
    check = True
    for j in range(1, n):
      if works_li[0]['val'] < works_li[j]['val']:
        check = False
        works_li.append(works_li.pop(0))
        break

    if check : 
        n -= 1
        if works_li[0]['id'] == m : 
          turn += 1
          break
        else : 
          turn += 1
          works_li.pop(0)
    
  print(turn)
