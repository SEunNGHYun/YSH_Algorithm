import sys

input = sys.stdin.readline

n, k = map(int, input().split())
pack = [0 for _ in range(k + 1)]
w_pack = []
v_pack = []

for _ in range(n):
  w, v = map(int, input().split())
  w_pack.append(w)
  v_pack.append(v)

for i in range(n):
  for j in range(k, w_pack[i] - 1, -1):
    pack[j] = max(pack[j], pack[j - w_pack[i]] + v_pack[i])
print(pack[k])