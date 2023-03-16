import sys

input = sys.stdin.readline

t = int(input())
t_li = []
max_t = -1

for _ in range(t):
    n = int(input())
    t_li.append(n)
    if max_t < n:
        max_t = n  # 입력값중에 가장 큰 수

sosu_li = [True] * (max_t + 1)  # 0 ~ 최댓값까지의 수와 인덱스 같은 배열 선언
sosu_li[1] = False  # 1일 걍우 모든 경우의 약수이니 False 넣음


def sosu(n):
    global sosu_li
    sqrt = int(n ** (0.5)) + 1
    count = 0
    for i in range(2, sqrt):  # i가 i의 배수인 것을 찾아 False로 변경
        if sosu_li[i]:
            for j in range(i+i, max_t+1, i):
                sosu_li[j] = False

            # 소수안 값은 True인 것으로 남는다.
sosu(max_t)

for n in t_li:
    count = 0
    for i in range(2, (n//2) + 1):
        if sosu_li[i] and sosu_li[n-i]:
            count += 1
    print(count)
