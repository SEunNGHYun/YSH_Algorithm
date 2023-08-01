import sys

input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
  b = input().strip()
  if b in books:
    books[b] = books[b] + 1
  else:
    books[b] = 1

res = {val[0] : val[1] for val in sorted(books.items(), key = lambda x: (-x[1], x[0]))}
res_key = list(res.keys())

print(res_key[0])