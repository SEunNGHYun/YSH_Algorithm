def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]  # bridge에 제한 수 만큼 선언
    bridge_w = 0
    while bridge:
        time += 1
        bridge_w -= bridge.pop(0)
        if truck_weights:
          # 럭이 다 지나가면 남은 bridge를 제거만 해준다.
            if bridge_w + truck_weights[0] <= weight:
                # 다음 트럭의 무게와 현재 다리에 있는 트럭들의 무게 합이 제한 무개를 넘는 지 확인
                t = truck_weights.pop(0)
                bridge.append(t)  # 다리에 트럭을 추가
                bridge_w += t
            else:
                bridge.append(0)  # 트럭이 아직 남아있으면 bridge의 제한수 만큼 길이를 유지

    return time
