from sys import stdin

def bound(carrots_x,carrots_y):
    y_low = min(carrots_y)
    y_high = max(carrots_y)
    x_low = min(carrots_x)
    x_high = max(carrots_x)
    return 2 * (y_high - y_low + x_high - x_low + 4)

if __name__=="__main__":
    N,M,K = map(int,input().strip().split())
    carrots_x = []
    carrots_y = []
    
    for i in range(K):
        x,y = map(int,stdin.readline().strip().split())
        carrots_x.append(x)
        carrots_y.append(y)
    
    print(bound(carrots_x,carrots_y))
    
# ============================================================

from sys import stdin

if __name__=="__main__":
    n = int(input())
    golds = list(map(int,stdin.readline().strip().split()))
    
    results = sum(golds[0:6])
    
    for i in range(n-5):
        for j in range(i+3,n-2):
            results = max(results,sum(golds[i:i+3])+sum(golds[j:j+3]))
    
    print(results)

# ============================================================
# N : 새로, M : 가로
from sys import stdin

def movement(x,y):
    if floor[x][y] == 1:
        return x-1,y
    elif floor[x][y] == 2:
        return x,y-1
    elif floor[x][y] == 3:
        return x,y+1
    else:
        return x+1,y


def check_in_and_out(N,M,floor,x,y):
    
    path = []
    cycle = []
    for _ in range(3*N*M):  # 여기에서 내가 뭔가 고려를 하지 않은 것이 있는데... 왜 3*N*M이어야되지..
        # print(x,y)
        
        if x<0 or y<0 or x>=N or y>=M:
            return -1
        
        if [x,y] not in path:
            path.append([x,y])
        else:
            if [x,y] not in cycle:
                cycle.append([x,y])
            else:
                return len(cycle)
        
        x,y = movement(x,y)
        
    
    
    
    return 

floor = []

if __name__=="__main__":
    N,M = map(int,input().strip().split())
    
    for _ in range(N):
        floor.append(list(map(int,stdin.readline().strip().split())))
        
    x,y = map(int,input().strip().split())
    
    print(check_in_and_out(N,M,floor,x-1,y-1))

# ============================================================
# 직원이 살고 있는 집의 위치가 서로 겹치는 경우는 없다.
from sys import stdin

if __name__=="__main__":
    n = int(input())
    people = list(map(int,stdin.readline().strip().split()))
    
    people = sorted(people)
    
    if n%2 == 1:
        print(1)
    else:
        print(people[n//2] - people[n//2 - 1] + 1)

# ============================================================
from sys import stdin

if __name__=="__main__":
    N = int(input())
    nums = list(map(int,stdin.readline().strip().split()))
    
    leng = [1 for _ in range(N)]
    
    for i in range(1,N):
        for j in range(i):
            if nums[j]<nums[i]:
                leng[i] = max(leng[i],leng[j]+1)
    
    print(N - max(leng))
