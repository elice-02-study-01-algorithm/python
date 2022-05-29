from sys import stdin

R,C,K = map(int,stdin.readline().strip().split())
# move : U = up, D = down, R = right, L = left.

floor = [stdin.readline().strip() for _ in range(R)]
di = {'U':(-1,0),'D':(1,0),'R':(-1,0),'L':(1,0)}  #elt : d
choice = [K,K]  # nbr of - clockwise_turn, counterclockwise_turn.
d = di[floor[0][0]]

def movement(R,C,floor,current,di,d):
    # floor를 넘어가는 케이스.
    if min(current[0]+di[d][0],current[1]+di[d][1]) < 0 or current[0]+di[d][0] > R or current[1]+di[d][1] > C:
        return 0 # 땡!
    
    #도착했다면.
    elif current[0]+di[d][0]== len(floor) and current[1]+di[d][1] == len(floor[0]):
        return 1
    
    #두 가지가 아닌 경우.. 즉, 다음턴!
    else:
        return (current[0]+d[0],current[1]+d[1])

while True:
    result = (0,0)
    if result == 0:
        print('No')
        exit(0)
    
    if result == 1:
        print('Yes')
        exit(0)
    
    result = movement(R,C,floor,result,di,d)
    d = di[floor[result[0]][result[1]]]
    print(d)