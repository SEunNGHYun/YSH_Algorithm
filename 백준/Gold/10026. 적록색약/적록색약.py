import sys
from collections import deque

input = sys.stdin.readline

# n, m = map(int, input().split())
# result = []
# move = ((0,1), (1,0), (-1, 0), (0, -1), (1,1), (1, -1), (-1, -1), (-1, 1))
# while n > 0 and m > 0:
#   feild = []
#   visited = [[0] * n for _ in range(m)]
#   count = 0
  
#   for _ in range(m):
#     feild.append(list(map(int, input().strip().split())))

#   for i in range(m):
#     for j in range(n):
#       if visited[i][j] == 0 and feild[i][j] == 1:
#         count += 1
        
#         q = deque([(i, j)])
#         visited[i][j] = 1
#         while q :
#           ci, cj = q.popleft()
          
#           for mi, mj in move :
#             xi, xj = (mi + ci), (mj + cj)
#             if 0<=xi<m and 0<=xj<n and visited[xi][xj] == 0 and feild[xi][xj] == 1:
#               q.append((xi, xj))
#               visited[xi][xj] = 1
              
#   result.append(count)
#   n, m = map(int, input().split())
  
# for val in result:
#   print(val)

n = int(input())
color = []
result_1 = []
for _ in range(n):
  color.append(list(input().strip()))

visted_1 = [[False] * n for _ in range(n)]
visted_2 = [[False] * n for _ in range(n)]
move = ((0,1), (0, -1), (1, 0), (-1, 0))
cnt_1, cnt_2 = 0, 0

for i in range(n):
  for j in range(n):
    if (not visted_1[i][j]):
      cnt_1 += 1
      c = color[i][j]
      q = deque([(i,j)])
      visted_1[i][j] = True
      
      while q:
        ci, cj = q.popleft()
        
        for mi, mj in move:
          xi,xj = (ci + mi), (cj + mj)
          if (0<=xi<n) and (0<=xj<n) and (not visted_1[xi][xj]) and color[xi][xj] == c:
            q.append((xi,xj))
            visted_1[xi][xj] = True
            
umm = ('R', 'G')

for i in range(n):
  for j in range(n):
    if (not visted_2[i][j]):
      cnt_2 += 1
      c = color[i][j]
      q = deque([(i,j)])
      visted_2[i][j] = True
      
      while q:
        ci, cj = q.popleft()
        
        for mi, mj in move:
          xi,xj = (ci + mi), (cj + mj)
          if (0<=xi<n) and (0<=xj<n) and (not visted_2[xi][xj]) :
            if (c in umm):
              if (color[xi][xj] in umm):
                q.append((xi,xj))
                visted_2[xi][xj] = True
            elif color[xi][xj] == c:
              q.append((xi,xj))
              visted_2[xi][xj] = True

print(cnt_1, cnt_2)