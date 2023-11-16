def solution(hp):
    count = 0
    while hp > 0:
        if (hp >= 5):
            hp -= 5
            count += 1
            continue
        elif (hp >= 3):
            hp -= 3
            count += 1
            continue
        elif (hp >= 1):
            hp -= 1
            count += 1
            continue
    return count