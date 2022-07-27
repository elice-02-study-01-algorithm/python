# https://school.programmers.co.kr/learn/courses/30/lessons/92342

# ! bitmasking

def solution(n, info):
    answer = []
    get_score = [i+1 for i in info]
    diff_score = 0
    
    for subset in range(1,1<<10):
        ryan = 0
        apeach = 0
        arr = [0 for _ in range(11)]
        
        for i in range(10):
            if subset & (1<<i):
                ryan += 10-i
                arr[i] = get_score[i]
            elif info[i] != 0:
                apeach += 10-i
                
        if sum(arr) > n:
            continue
        
        arr[10] = n-sum(arr)
        
        if ryan-apeach == diff_score:
            answer.append(arr)
        elif ryan-apeach > diff_score:
            answer = [arr]
            diff_score = ryan-apeach
    
    if diff_score == 0:
        return [-1]
    
    return answer[-1]
    


# n, info = 5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# print(solution(n, info))

