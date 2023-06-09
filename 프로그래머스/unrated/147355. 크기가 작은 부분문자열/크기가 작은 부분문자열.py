def solution(t, p):
    leng_p = len(p) 
    p = int(p)
    leng_t = len(t) + 1
    t_num_arr = []
    for i in range(leng_t - leng_p):
        num = int(t[i:i+leng_p])
        if num <= p : 
            t_num_arr.append(num)
    return len(t_num_arr)