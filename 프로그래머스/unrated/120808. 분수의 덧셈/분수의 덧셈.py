def solution(numer1, denom1, numer2, denom2):
    answer = []
    def check (n1, n2):
        a, b , c, = 0,0,0
        if (n1 > n2):  # a가 큰수 b는 작은 수로 고정
            a = n1
            b = n2
        else:
            a = n2
            b = n1

        while (b != 0):
            c = a % b
            a = b
            b = c
            
        return a
        # a가 최대 공약수
    
    mom = (denom1 * denom2) // check(denom1, denom2)
    bro = (numer1 * (mom//denom1)) + (numer2 * (mom//denom2))
    d = check(bro, mom)
    answer = [bro // d, mom // d]
    
    return answer

