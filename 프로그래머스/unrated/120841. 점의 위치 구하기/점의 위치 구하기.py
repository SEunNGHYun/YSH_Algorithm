def solution(dot):
    def check (p) :
        if (p < 0):
            return -1
        else :
            return 1
    dot = [check(dot[0]), check(dot[1])]
    if (dot[0] == -1 and dot[1] == -1):
        return 3
    elif (dot[0] == 1 and dot[1] == 1):
        return 1
    elif (dot[0] == -1 and dot[1] == 1):
        return 2
    elif (dot[0] == 1 and dot[1] == -1):
        return 4
        