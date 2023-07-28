def solution(array, commands):
    result = []
    for com in commands:
        i, j, k = (com[0] - 1), com[1], com[2]
        arr = array[i:j]
        arr.sort()
        result.append(arr[k-1])
    return result
        