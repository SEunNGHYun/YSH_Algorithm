import sys

input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    s = list(input().strip())
    stack = [s[0]]
    leng_r = len(s)
    if (leng_r % 2) == 0:
        for i in range(1, leng_r):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        count += 1
print(count)
