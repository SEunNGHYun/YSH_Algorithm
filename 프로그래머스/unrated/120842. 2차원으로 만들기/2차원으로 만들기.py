def solution(num_list, n):
    answer = []
    bucket = []
    for i in range(len(num_list)):
        bucket.append(num_list[i])
        if ((i + 1) % n) == 0:
            answer.append(bucket)
            bucket = []
        
    return answer