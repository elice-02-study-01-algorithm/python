
# 3번 아몰랑 50점 시마이.. 뭐가 문제인지 모르겠다.

order = [1,4,5,3,2]

from collections import deque

def solution(order):
    answer = 0
    
    done = deque(order)
    aim = done.popleft()
    sub_trail = deque()
    
    for i in range(1,len(order)+1):
        
        if i == aim:
            aim = done.popleft()
            answer += 1
        elif sub_trail and sub_trail[-1] == aim:
            while sub_trail[-1] == aim:
                sub_trail.pop()
                aim = done.popleft()
                answer += 1
        elif aim < i and sub_trail and sub_trail[-1] != aim:
            return answer
        else:
            sub_trail.append(i)
    
    while sub_trail:
        if sub_trail[-1] != aim:
            break

        sub_trail.pop()
        answer += 1
        
        if len(done) == 0:
            break
        aim = done.popleft()
        
    return answer

print(solution(order))
