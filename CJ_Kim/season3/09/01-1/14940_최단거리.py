mapN, mapM = map(int, input().split())
mapInfo = []
visited = [[0 for _ in range(mapM)] for _ in range(mapN)]
distance = [[-1 for _ in range(mapM)] for _ in range(mapN)]
startDot = ()

for i in range(mapN):
    eachRow = list(map(int, input().split()))
    for j in range(len(eachRow)):
        if eachRow[j] == 2:
            startDot = (i, j)
    mapInfo.append(eachRow)

dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def BFS(mapInfo, startDot):
    queue = [startDot]
    visited[startDot[0]][startDot[1]] = 1
    distance[startDot[0]][startDot[1]] = 0
    while queue:
        curN, curM = queue.pop(0)
        for i in range(4):
            newR, newC = curN+dr[i], curM+dc[i]
            if 0<=newR<mapN and 0<=newC<mapM and visited[newR][newC] == 0:
                if mapInfo[newR][newC] == 1:
                    distance[newR][newC] = distance[curN][curM] + 1
                    visited[newR][newC] = 1
                    queue.append([newR, newC])
                elif mapInfo[newR][newC] == 0: 
                    distance[newR][newC] = 0

BFS(mapInfo, startDot)

for i in range(mapN):
    for j in range(mapM):
        if distance[i][j] == -1 and mapInfo[i][j] == 0:
            distance[i][j] = 0
for eachRow in distance:
    print(*eachRow)

'''
반례
3 2
0 2
0 0
0 0

현재 결과
0 0
-1 0
-1 -1

결과
0 0
0 0
0 0
'''