# 다시 칠해야하는 최솟 값
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
count = []

for i in range(N):
    row = input()
    board.append(row)
# board 저장

for i in range(N - 7):
    for j in range(M-7):
        first_w = 0
        first_b = 0
        for h in range(i, i+8):
            for w in range(j, j+8):
                if (w+h) % 2 == 0:
                    if board[h][w] != 'W':
                        first_w += 1
                    if board[h][w] != 'B':
                        first_b += 1
                else:
                    if board[h][w] != 'B':
                        first_w += 1
                    if board[h][w] != 'W':
                        first_b += 1
        count.append(first_w)
        count.append(first_b)

print(min(count))
