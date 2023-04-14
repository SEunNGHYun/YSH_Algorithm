def solution(people, limit):
    # limit <= 되는 값이 구명 보트 탑승
    # 구명보트에 탑승할 수 있는 사람의 수는 2명으로 제한 있음
    boat = 0
    people.sort() # 오름차순으로 정렬
    i = 0
    j = len(people) - 1
    while i <= j:
        boat += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return boat
                
    