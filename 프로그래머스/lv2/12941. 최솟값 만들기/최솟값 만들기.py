def solution(A, B):
    answer = 0

    a_sort = sorted(A)
    b_sort = sorted(B, reverse=True)
    print(a_sort, b_sort)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(A)):
        answer += a_sort[i] * b_sort[i]

    return answer
