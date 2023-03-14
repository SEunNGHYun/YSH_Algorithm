
for _ in range(100):
  try:
    s = input()
    big = small = num = space = 0
    for i in range(len(s)):
        if s[i] == ' ':
            space += 1
        elif 48 <= ord(s[i]) and ord(s[i]) <= 58:
            num += 1
        elif 65 <= ord(s[i]) and ord(s[i]) <= 90:
            big += 1
        elif 97 <= ord(s[i]) and ord(s[i]) <= 122:
            small += 1
    print(small, big, num, space)
  except EOFError:
        break
