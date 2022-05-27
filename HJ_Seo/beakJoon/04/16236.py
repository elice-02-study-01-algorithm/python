from sys import stdin

def min_leng_target(field,location,sharklvl):
    loc_dict ={0:[location]}
    
    di = [(-1,0),(0,-1),(0,1),(1,0)]
    leng = 0
    target = [-1,-1]
    
    isend = False
    field_leng = len(field)-1 #n = 6일 때 field_leng도 6, but list의 마지막은 5이므로.
    
    while True:
        x = sum(field,[]) # ! min == 0...
        while 0 in x:
            x.remove(0)
        # print(x)
        # print(sharklvl)
        if min(x) >= sharklvl: #타겟이 있는지 체크.
            return True,leng,field,location
        
        maxdirc = max(loc_dict.keys())
        temp = [] # 값 저장하기.
        for i in loc_dict[maxdirc]:
            for j in di:
                if min(i[0]+j[0],i[1]+j[1]) < 0 or max(i[0]+j[0],i[1]+j[1]) > field_leng or field[i[0]+j[0]][i[1]+j[1]] > sharklvl or [i[0]+j[0],i[1]+j[1]] in sum(loc_dict.values(),[]):
                    # 1,2 : 맵을 벗어남., 3 : 위치에 존재한 먹이의 레벨이 상어레벨보다 높음., 4 : 이미 들른 위치.
                    continue
                
                # 위의 경우가 아니면 갈 수 있는 경우.
                if maxdirc+1 not in loc_dict.keys(): 
                    loc_dict[maxdirc+1] = []
                loc_dict[maxdirc+1].append([i[0]+j[0],i[1]+j[1]])
                
                if field[i[0]+j[0]][i[1]+j[1]] != 0 and field[i[0]+j[0]][i[1]+j[1]] < sharklvl: #먹이 발견.
                    temp.append([i[0]+j[0],i[1]+j[1]])
                    
        if temp:
            temp = sorted(temp)
            target = temp[0]
            leng = maxdirc + 1
            # print('sharklvl =',sharklvl)
            # print('temp, leng =',temp, leng)
            break

    field[target[0]][target[1]] = 9 #타겟에 도착한 상황.
    field[location[0]][location[1]] = 0
    location = target
    
    return isend,leng,field,location #시점부터 타겟까지의 길이, 타겟에 도착했을 때 필드 return

n = int(stdin.readline().strip())
field = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

sharklvl = 2
eat_cnt = 0
moveleng = 0
location = [-1,-1]
for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            location = [i,j]
            break

while True:  
    isend,leng,field,location = min_leng_target(field,location,sharklvl)
    # print('return값 =', isend,leng,field,location)
    if isend:
        break
    
    moveleng += leng
    eat_cnt += 1
    
    if eat_cnt == sharklvl:
        sharklvl += 1
        eat_cnt = 0

print(moveleng)

# 아니 이건 왜 시간초과가 뜨냐??ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ


# ! 좋은 코드 지우기 아까워 남겨놓음.
# from sys import stdin

# def sona(field,sharklvl): # 상어 레벨에 따라 움직일 수 있는 위치 및 먹이 탐지.
#     poss_move = [[1 for _ in range(n)] for _ in range(n)]
#     location = [-1,-1]
#     for i in range(n):
#         for j in range(n):
#             if field[i][j] == 9: 
#                 location = [i,j]
#                 poss_move[i][j] = 3  #상어 위치.
#             elif field[i][j] == sharklvl or field[i][j] == 0: 
#                 pass
#             elif field[i][j] < sharklvl: 
#                 poss_move[i][j] = 2  #먹이 위치.
#             else:
#                 poss_move[i][j] = 0  #위치한 먹이의 레벨이 상어보다 높은 경우.

#     return poss_move,location

# def min_leng_target(poss_move,location,field):
#     loc_dict ={0:[location]}
    
#     di = [(-1,0),(0,-1),(0,1),(1,0)]
#     leng = 0
#     target = [0,0]
#     field_leng = len(poss_move)-1 #n = 6일 때 field_leng도 6, but list의 마지막은 5이므로.
    
#     while True:
#         maxdirc = max(loc_dict.keys())
#         temp = []
#         for i in loc_dict[maxdirc]:
#             for j in di:
#                 if min(i[0]+j[0],i[1]+j[1]) < 0 or max(i[0]+j[0],i[1]+j[1]) > field_leng or poss_move[i[0]+j[0]][i[1]+j[1]] == 0 or [i[0]+j[0],i[1]+j[1]] in sum(loc_dict.values(),[]):
#                     continue
                
#                 if maxdirc+1 not in loc_dict.keys():
#                     loc_dict[maxdirc+1] = [[i[0]+j[0],i[1]+j[1]]]
#                 else:
#                     loc_dict[maxdirc+1] += [[i[0]+j[0],i[1]+j[1]]]
                
#                 temp.append(poss_move[i[0]+j[0]][i[1]+j[1]])
        
#         if 2 in temp:
#             leng = maxdirc+1
            
#             target_lst=[]
#             for i in range(len(temp)):
#                 if temp[i] == 2:
#                     target_lst.append(loc_dict[leng][i])
            
#             target = sorted(target_lst,key = lambda x: (x[0],x[1]))[0]
#             break
    
#     field[target[0]][target[1]] = 9 #타겟에 도착한 상황.
#     field[location[0]][location[1]] = 0
    
#     return leng,field #시점부터 타겟까지의 길이, 타겟에 도착했을 때 필드 return

# n = int(stdin.readline().strip())
# field = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

# sharklvl = 2
# eat_cnt = 0
# moveleng = 0

# poss_move,location = sona(field,sharklvl)

# while 2 in sum(poss_move,[]):
#     leng,field = min_leng_target(poss_move,location,field)
#     moveleng += leng
#     eat_cnt += 1
    
#     if eat_cnt == sharklvl:
#         sharklvl += 1
#         eat_cnt = 0
    
#     poss_move,location = sona(field,sharklvl)
    
# print(moveleng)
# ! 시간 초과.... 알고리즘은 맞는데..ㅠ --> sona를 없애고 bfs 로직상에서 갈 수 없는 곳을 sharklvl을 통해 처리하면 통과할듯.