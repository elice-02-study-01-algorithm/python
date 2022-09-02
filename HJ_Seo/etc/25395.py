from sys import stdin

N,S = map(int,stdin.readline().strip().split())

init_location = tuple(map(int,stdin.readline().strip().split()))
car_move = tuple(map(int,stdin.readline().strip().split()))

def cars(loc,move,S):
    tmp = {S}
    left = loc[S-1] - move[S-1]
    right = loc[S-1] + move[S-1] 
    
    for i in range(S-2,-1,-1):
        if loc[i] >= left:
            tmp.add(i+1)
            # print(i+1)
            left = min(left,loc[i] - move[i])
            right = max(right,loc[i] + move[i])
        else:
            break
    
    for i in range(S,N):
        if loc[i] <= right:
            tmp.add(i+1)
            # print(i+1)
            right = max(right,loc[i] + move[i])
            left = min(left,loc[i] - move[i])
        else:
            break
        
    for i in range(S-2,-1,-1):
        if loc[i] >= left:
            tmp.add(i+1)
            # print(i+1)
            left = min(left,loc[i] - move[i])
            right = max(right,loc[i] + move[i])
        else:
            break
    
    for i in range(S,N):
        if loc[i] <= right:
            tmp.add(i+1)
            # print(i+1)
            right = max(right,loc[i] + move[i])
            left = min(left,loc[i] - move[i])
        else:
            break

    return tmp

print(*cars(init_location,car_move,S))

# ! 고려해야 할 것!! --> 위치가 낮은데 연료량이 압도적으로 높아 비교대상보다 더 멀리 갈 수 있을 때.