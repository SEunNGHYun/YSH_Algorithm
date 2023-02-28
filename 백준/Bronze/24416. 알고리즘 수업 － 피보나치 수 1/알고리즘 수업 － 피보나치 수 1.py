
num = int(input())
fb = [1 for _ in range(num)]


def fib(n):
    for i in range(2, num):
        fb[i] = fb[i-1]+fb[i-2]

    return fb[num-1]


count1 = fib(num)

print(count1, num - 2)
