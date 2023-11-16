def solution(balls, share):
    def p (num):
        result = 1
        while num > 1:
            result *= num
            num -= 1
        return result
    return p(balls) // (p(balls-share) * p(share))