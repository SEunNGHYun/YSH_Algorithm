import sys

input = sys.stdin.readline

s1, s2, s3 = map(int, input().split())

arr = [0 for _ in range((s1+s2+s3) + 1)]

for i in range(1, s1 + 1):
  for j in range(1, s2 + 1):
    for k in range(1, s3 + 1):
      arr[i+j+k] += 1


m_val = max(arr)

for i in range(1, (s1+s2+s3)+1) :
  if arr[i] == m_val :
    print(i)
    break