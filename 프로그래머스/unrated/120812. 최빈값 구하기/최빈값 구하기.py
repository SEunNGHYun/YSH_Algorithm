def solution(array):
    dict_arr = {}
    for a in array:
        if a in dict_arr:
            dict_arr[a] += 1
        else:
            dict_arr[a] = 1
    compare = 0
    result = 0
    for key, val in dict_arr.items():
        if val > compare :
            compare = val
            result = key
        elif val == compare : 
            result = -1
            compare = val
    return result