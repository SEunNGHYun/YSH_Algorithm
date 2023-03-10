import sys

input = sys.stdin.readline

left = list(input().strip())
n = int(input())

right = []

for _ in range(n):
    command = input().split()
    if command[0] == 'L':
        if len(left) > 0:
            right.append(left.pop())
    elif command[0] == 'D':
        if len(right) > 0:
            left.append(right.pop())
    elif command[0] == 'B':
        if len(left) > 0:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

right = list(reversed(right))

print(''.join(map(str, (left + right))))

# print(''.join(map(str, str_arr)))
