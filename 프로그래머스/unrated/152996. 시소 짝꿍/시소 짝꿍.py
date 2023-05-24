
from collections import Counter


def solution(weights):
    answer = 0
    w_counter = Counter(weights)

    for w, c in w_counter.items():
        if c >= 2:  # 같은 무게가 2개 이상이면 nC2로 계산 가능
            answer += (c * (c - 1)) // 2
    weights = set(weights)  # 같은 무게를 가진 (중복 )제거

    for w in weights:
        if (w * 2/3) in weights:
            answer += w_counter[w*2/3] * w_counter[w]
        if (w * 2/4) in weights:
            answer += w_counter[w*2/4] * w_counter[w]
        if (w * 3/4) in weights:
            answer += w_counter[w*3/4] * w_counter[w]

    return answer


print(solution([100, 180, 360, 100, 270]))
