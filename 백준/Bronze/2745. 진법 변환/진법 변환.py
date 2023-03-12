import sys

input = sys.stdin.readline

val, B = map(str, input().split())
dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
        'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
        'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
B = int(B)
result = 0
leng = len(val) - 1
i = 0

while leng >= 0:
    if val[leng] in dict:
        result += (B ** i) * dict[val[leng]]
    else:
        result += (B ** i) * int(val[leng])
    leng -= 1
    i += 1

print(result)
