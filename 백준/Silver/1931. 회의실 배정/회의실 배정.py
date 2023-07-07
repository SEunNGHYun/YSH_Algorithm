
import sys

input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n) :
  room.append(tuple(map(int, input().split())))

room.sort(key= lambda x:x[0])
room.sort(key= lambda x:x[1])

end = room[0][1]
count = 1

for i in range(1, n):
  if end <= room[i][0]:
    count += 1
    end = room[i][1]

print(count)