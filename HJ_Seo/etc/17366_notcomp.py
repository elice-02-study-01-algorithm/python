# d1
# S와 T로 나눌 수 있다는 설명.. arr를 쪼갤 방법을 생각해보자..
# ex. arr == ST.. then, s in S & T in T t-s = t-T[0] + S[-1]-s + 1
# index단위로 S와 T를 구분할 수 있을 것 같은데..
# 현재 코드는 돌아가지 않을 가능성이 높다..!.. space의 floor을 체크한 상태로 나누었기 때문.  


from sys import stdin
import math

def check_min(start,end,portal,result):
    if abs(end - start) == 2:
        return 2
    
    for st,en in portal.items():
        if abs(st-start)+abs(end-en)+2 < result:
            # print(st,en)
            result = abs(st-start)+abs(end-en) + check_min(st,en,portal,result)
            
    return result

def check_space(start,end,portals,STdiff):
    # start와 end는 항상 정방향으로.
    if start > end:
        temp = start
        start = end
        end = temp
    
    result = math.inf
    interval_space = []
    
    for i,start_interval,end_interval in enumerate(STdiff.items()):
        
        # 만약 start와 end 가 한 space 안에 있다면 space 내에서 계산하기.
        if (start_interval <= start) and (end <= end_interval):
            result = check_min(start,end,portals[i],result)
            return result
        
        # 만약 아니라면..
        elif start_interval <= start:
            if end_interval < end:
                break
            
            interval_space.append([i,start_interval,end_interval])

    # start가 들어있는 space의 start와 끝 사이의 min값 + end가 들어있는 space의 end와 space의 시작 사이의 min값 + 스페이스 점프 횟수 더해주기.
    result = check_min(start,interval_space[0][2],portals[interval_space[0][0]],result) 
    + check_min(interval_space[-1][1],end,portals[interval_space[-1][0]],result)
    + 2*(len(interval_space) - 2)
    
    #space 사이의 모든 간격 더해주기.
    for i in range(1,len(interval_space)):
        result += interval_space[i][1] - interval_space[i-1][2]  

    return result


N,Q = map(int,input().strip().split())
arr = stdin.readline()

open = []
portals = []
STdiff = {}
# STinterval = []
portal = {}
for i in range(N):
    if arr[i] == '(':
        open.append(i)
    elif arr[i] == ')':
        j = open.pop()
        
        if abs(i-j) <=2:
            continue
            # 포탈의 길이가 2 이하라면 안씀.. 고려대상에서 제외.
        else:
            portal[min(i,j)] = max(i,j)
            # key값이 무조껀 앞선 수.
        
        if len(open)==0:
            STdiff[min(i,j)] = max(i,j)
            portals.append(portal)
            
# print(STdiff)
# testcase: STdiff == {1: 11}
# hard counter case.. STdiff == {1: 11, 14: 59, 60: 95}
# 공백공간의 문제.

for i in range(Q):
    start, end = map(int,stdin.readline().strip().split())
    if abs(start-end)<=2:
        print(abs(start-end))
    else:
        print(check_space(start-1,end-1,portal,STdiff))
    # 이제 탐색을 해보자. 0부터 시작이므로 각각 1을 뺀 값을 input으로 넣어줌.


"""
input : 
12 3
.(.()..(.).)
7 10
11 1
4 9  

output : 
3
4
5

# 예시는 맞음. but 시간초과..
"""