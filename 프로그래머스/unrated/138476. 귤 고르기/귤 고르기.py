def solution(k, tangerine):
    tan_set = set(tangerine)
    tan_dict = {}
    count_k = i = answer = 0
    for t in tangerine:
        if t in tan_dict:
            tan_dict[t] += 1
        else:
            tan_dict[t] = 1
    tan_dict = sorted(tan_dict.items(), key = lambda item: item[1], reverse = True)
    # 갯수 기준으로 sort 시킴
    while True:
        count_k += tan_dict[i][1]
        answer += 1

        if count_k >= k :
            break
        else :
            i +=1
    return answer
