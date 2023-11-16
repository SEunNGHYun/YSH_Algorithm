def solution(rsp):
    win = { '2' : '0', '0': '5', '5': '2'}
    answer = ''
    for hand in rsp:
        answer += win[hand]
    return answer