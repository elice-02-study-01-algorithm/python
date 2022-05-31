from sys import stdin

R,C,K = map(int,stdin.readline().strip().split())
# move : U = up, D = down, R = right, L = left.

floor = [stdin.readline().strip() for _ in range(R)]
di = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}  #elt : d
choice = [K,K]  # nbr of - clockwise_turn, counterclockwise_turn.
d = floor[0][0]



# ! movement without using choice.
def movement(R,C,current,di,d):
    # floor를 넘어가는 케이스.
    # print(current,di[d])
    new_loc = (current[0]+di[d][0],current[1]+di[d][1])
    
    if min(new_loc[0],new_loc[1]) < 0 or new_loc[0] >= R or new_loc[1] >= C:
        return 0 # 땡!
    
    #도착했다면.
    elif new_loc[0] == R and new_loc[1] == C:
        return 1
    
    #두 가지가 아닌 경우.. 즉, 다음턴!
    else:
        return new_loc

result = (0,0)
while True:
    result = movement(R,C,floor,result,di,d)
    print(result)
    
    if result == 0:
        print('No')
        exit(0)
    
    if result == 1:
        print('Yes')
        exit(0)

    d = floor[result[0]][result[1]]
    print(d)