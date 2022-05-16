from sys import stdin

n = int(stdin.readline().strip())

field = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

location = [-1,-1]
sharklvl = 2
eat_cnt = 0
initial_target = []
poss_move = [[1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            location = [i,j]
        elif field[i][j] == 1:
            initial_target.append([i,j])
        else:
            poss_move[i][j] = 0

initial_target = sorted(initial_target, key = lambda x: (abs(x[0]-location[0])+abs(x[1]-location[1]),x[0],x[1]))
# print(initial_target)

def movement(location,sharklvl,field,eat_cnt,target_lst):
    new_target_lst = []
    
    
    
    target_lst = sorted(new_target_lst, key = lambda x: (abs(x[0]-location[0])+abs(x[1]-location[1]),x[0],x[1]))
    
    return location,sharklvl,field,eat_cnt,target_lst