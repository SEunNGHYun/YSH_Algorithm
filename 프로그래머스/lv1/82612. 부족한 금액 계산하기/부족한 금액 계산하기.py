def solution(price, money, count):
    total_price = 0
    for m in range(1, count+1):
        total_price += price * m
    if (total_price - money) >= 0 :
        return (total_price - money)
    else:
        return 0