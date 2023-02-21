import sys

input = sys.stdin.readline

result = ''

size = int(input())

for i in range((size // 4)):
    result += 'long '

result += 'int'

print(result)
