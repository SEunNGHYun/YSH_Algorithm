

s = input()
result = ''

for i in range(len(s)):
    asc2 = ord(s[i])
    if 65 <= asc2 and asc2 <= 90:  # 대문자
        if asc2 + 13 > 90:
            asc2 = asc2 - 13
        else:
            asc2 = asc2 + 13
    elif 97 <= asc2 and asc2 <= 122:  # 소문자
        if asc2 + 13 > 122:
            asc2 = asc2 - 13
        else:
            asc2 = asc2 + 13
    result += chr(asc2)
print(result)
