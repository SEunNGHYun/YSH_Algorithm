import sys

input = sys.stdin.readline

N, B = map(int, input().split())
C = 0
result = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while N > 0:
    C = N % B
    N = N // B
    if C >= 10:
        result.append(alphabet[C-10])
    else:
        result.append(str(C))

for i in result[::-1]:
    print(i, end='')
print()