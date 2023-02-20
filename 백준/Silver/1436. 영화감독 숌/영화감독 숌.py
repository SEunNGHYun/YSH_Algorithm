import sys

input = sys.stdin.readline

N = int(input())
movie_title = 666
count = 0

while count < N:
    if '666' in str(movie_title):
        count += 1
    movie_title += 1

print(movie_title - 1)
