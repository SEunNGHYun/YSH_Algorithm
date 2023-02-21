import sys
import math
input = sys.stdin.readline

N = int(input())
ave = 0  # 산술평균
nums = []
numDic = {}  # 최빈값할 딕셔너리

for _ in range(N):
    num = int(input())
    nums.append(num)
    ave = ave + num
    # input값의 빈도수 설정
    if num not in numDic:  # 갯수 세는 딕셔너리
        numDic[num] = 1
    else:
        numDic[num] = numDic[num] + 1

sorted_dict = sorted(
    numDic.items(), key=lambda item: (item[1], item[0]), reverse=True)  # 빈도수를 기준으로 정렬

most_counting_numVal = sorted_dict[0][1]  # 가장 많은 빈도수 값의 Val
most_counting_numKey = sorted_dict[0][0]  # 가장 많은 빈도수 값의 key를 뽑음

if N > 1:
    # 동일한 빈도수 일 때
    if most_counting_numVal == sorted_dict[1][1]:
        test = [sorted_dict[0][0]]
        for i in range(1, len(sorted_dict)):
            if sorted_dict[i-1][1] == sorted_dict[i][1]:
                test.append(sorted_dict[i][0])
            else:
                break
        most_counting_numKey = sorted(test)[1]

nums.sort()  # 숫자 정렬

# key값이 정령된 딕셔너리 추출 value는 정렬 안됨
# for num in nums:


ave = ave / N
middleVal = nums[(N-1) // 2]
min = nums[0]
max = nums[N - 1]
rng = 0  # 범위

if min != max:  # 둘다 -일때, 하나만 -일 때,
    rng = max - min

rng = abs(rng)  # -값이 있을 수도 있으니 절댓값

print(round(ave))  # 산술평균 소수 첫째에서 반올림
print(middleVal)  # 중앙 값
print(most_counting_numKey)  # 최빈값
print(rng)  # 범위
