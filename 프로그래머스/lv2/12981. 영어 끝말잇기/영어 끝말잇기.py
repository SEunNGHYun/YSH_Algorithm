
def solution(n, words):

    answer = [0, 0]
    end_point = words[0][-1]
    db = [words[0]]
    turn = 1
    people = 1

    for i in range(1, len(words)):
        people += 1
        if people > n:
            people = 1
            turn += 1
        if words[i][0] == end_point and (words[i] not in db):
            # 직전 단어의 끝단어가 첫단어와 같은지 확인
            # 이전에 나온 단어인지 확인
            db.append(words[i])
            end_point = words[i][-1]
        else:
            answer[0] = people
            answer[1] = turn
            break

    return answer