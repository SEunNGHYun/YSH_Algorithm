
arr1 = [1, 1, 1, 1, 1]
arr2 = [4, 1, 2, 1]


def solution(ar, ta):

    count = 0
    sum_val = 0

    def de_sol(val, i):

        if i == len(ar):
            if ta == val:
                nonlocal count
                count += 1
                return
        else:
            de_sol(val + ar[i], i+1)
            de_sol(val - ar[i], i+1)

    de_sol(sum_val, 0)

    return count


print(solution(arr2, 4))
