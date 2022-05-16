from sys import stdin

n = int(stdin.readline().strip())
field = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

sharklvl = 2
eat_cnt = 0
moveleng = 0

def sona(field,sharklvl): # 상어 레벨에 따라 움직일 수 있는 위치 및 먹이 탐지.
    poss_move = [[1 for _ in range(n)] for _ in range(n)]
    location = [-1,-1]
    for i in range(n):
        for j in range(n):
            if field[i][j] == 9: 
                location = [i,j]
                poss_move[i][j] = 3  #상어 위치.
            elif field[i][j] < sharklvl: 
                poss_move[i][j] = 2  #먹이 위치.
            elif field[i][j] > sharklvl:
                poss_move[i][j] = 0  #위치한 먹이의 레벨이 상어보다 높은 경우.

    return poss_move,location

def min_leng_target(poss_move,location,field):
    def bfs(poss_move,loc_dict):
        di = [(-1,0),(0,-1),(0,1),(1,0)]
        leng = 0
        field_leng = len(poss_move)-1 #n = 6일 때 field_leng도 6, but list의 마지막은 5이므로.
        
        while True:
            maxdirc = max(loc_dict.keys())
            temp = []
            for i in loc_dict[maxdirc]:
                for j in di:
                    if min(i[0]+j[0],i[1]+j[1]) < 0 or max(i[0]+j[0],i[1]+j[1]) > field_leng or poss_move[i[0]+j[0]][i[1]+j[1]] == 0 or [i[0]+j[0],i[1]+j[1]] in sum(loc_dict.values(),[]):
                        continue
                    
                    if maxdirc+1 not in loc_dict.keys():
                        loc_dict[maxdirc+1] = [[i[0]+j[0],i[1]+j[1]]]
                    else:
                        loc_dict[maxdirc+1] += [[i[0]+j[0],i[1]+j[1]]]
                    
                    temp.append(poss_move[i[0]+j[0]][i[1]+j[1]])
            
            if 2 in temp:
                leng = maxdirc+1
                
                target = [-1,-1]
                temp2 = []
                for i in range(len(temp)):
                    if temp[i] == 2:
                        temp2.append(i)
                
                for i in range(len(temp2)):
                    temp2[i] = loc_dict[leng][temp2[i]]
                    
                target = sorted(temp2,key = lambda x: (x[0],x[1]))[0]
                # target = loc_dict[leng][temp.index(2)]
                
                return leng,target
        
    loc_dict ={0:[location]}
    leng,target = bfs(poss_move,loc_dict)
    
    field[target[0]][target[1]] = 9 #타겟에 도착한 상황.
    field[location[0]][location[1]] = 0
    return leng,field #시점부터 타겟까지의 길이, 타겟에 도착했을 때 필드 return


poss_move,location = sona(field,sharklvl)

while 2 in sum(poss_move,[]):
    leng,field = min_leng_target(poss_move,location,field)
    moveleng += leng
    eat_cnt += 1
    
    if eat_cnt == sharklvl:
        sharklvl += 1
        eat_cnt = 0
    
    poss_move,location = sona(field,sharklvl)
    
print(moveleng)
# ! 시간 초과.... 알고리즘은 맞는데..ㅠ