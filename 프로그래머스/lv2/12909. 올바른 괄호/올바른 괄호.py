

def solution(s_input):
    val = list()
    check = True

    for i in range(len(s_input)):
        if s_input[i] == ')':
            if len(val) > 0:
                val.pop()
            else:
                check = False
                break
        else:
            val.append(s_input[i])

    if check == True:
        if len(val) > 0:
            return False
        else:
            return True
    else:
        return False


