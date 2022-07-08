from sys import stdin,setrecursionlimit

setrecursionlimit(10**6)

def DFS(pmap,conn_map,in_map,stt,row,col):
    di = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    
    for i in di:
        move = (stt[0]+i[0],stt[1]+i[1])
        
        if min(move)<0 or move[0]>=row or move[1]>=col or pmap[move[0]][move[1]] == 0 or move in in_map:
            continue
        
        conn_map[-1].append(move)
        in_map.append(move)
        conn_map,in_map = DFS(pmap,conn_map,in_map,move,row,col)
    
    return conn_map,in_map

while True:
    col,row = map(int,stdin.readline().strip().split())
    
    if row == 0:
        break
    
    pmap = [tuple(map(int,stdin.readline().strip().split())) for _ in range(row)]
        
    conn_map = []
    in_map = []
    for i in range(row):
        for j in range(col):
            if pmap[i][j] == 0 or (i,j) in in_map:
                continue
            
            conn_map.append([(i,j)])
            in_map.append((i,j))
            conn_map,in_map = DFS(pmap,conn_map,in_map,(i,j),row,col)

    print(len(conn_map))

# ! recursionError 가 떠서 시간을 늘려줌. but code refactoring을 해서 줄일 수 있을듯 하다..