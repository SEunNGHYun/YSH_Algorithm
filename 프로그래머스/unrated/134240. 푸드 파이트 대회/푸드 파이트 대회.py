def solution(food):
    food_list = ''
    for i in range(1, len(food)):
        loop = food[i] // 2
        for _ in range(loop): 
            food_list += str(i)
    food_list += '0'
    food_list += food_list[len(food_list)-2::-1]
    return food_list
            