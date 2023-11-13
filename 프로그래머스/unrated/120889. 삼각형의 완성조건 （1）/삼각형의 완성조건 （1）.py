def solution(sides):
    sides.sort()
    long = sides[2]
    s_1, s_2 = sides[0], sides[1]
    if (s_1 + s_2) > long :
        return 1
    else:
        return 2