def de_zero(s):
    count = start = 0
    end = len(s) - 1
    half = end // 2
    for i in range(half + 1):
        if s[i] == '1':
            count += 1
        if i != (end - i):
            if s[end - i] == '1':
                count += 1
    return count, (len(s) - count)


def make_two(n):
    s = ''
    num = n
    while num >= 1:
        s = str(num % 2) + s
        num = num // 2

    return s


def solution(s):
    result = [0, 0]
    check = 0
    while s != '1':
        check, d_check = de_zero(s)
        print("check::", check, d_check)
        result[0] += 1
        result[1] += d_check
        s = make_two(check)
        print(s)
    return result
