count = 0


def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


N = int(input())
str_li = []

for _ in range(N):
    str_li.append(input())


for str in str_li:

    print(isPalindrome(str), end=' ')
    print(count)
    count = 0
