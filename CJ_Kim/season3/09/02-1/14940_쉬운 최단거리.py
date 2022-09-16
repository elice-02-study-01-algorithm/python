'''
########
# TRYI #
########
41376KB 756ms
'''
# 코드를 줄일 수록 시간이 예상치 못하게 더 나와서 매우 당황스럽습니다!

mapN, mapM = map(int, input().split())
mapInfo = []
visited = [[0 for _ in range(mapM)] for _ in range(mapN)]
distance = [[-1 for _ in range(mapM)] for _ in range(mapN)]
startDot = ()

for i in range(mapN):
    eachRow = list(map(int, input().split()))
    # map을 만들어줄 때 2이면 시작 포인트를 잡고, 0이면 결과값에 0으로 설정합니다.
    for j in range(len(eachRow)):
        if eachRow[j] == 2:
            startDot = (i, j)
        # 띠용? 시간 더 나오는 요인...!
        elif eachRow[j] == 0:
            distance[i][j] = 0
    mapInfo.append(eachRow)

dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

# 일반적인 BFS 처리와 동일합니다.
def BFS(mapInfo, startDot):
    queue = [startDot]
    visited[startDot[0]][startDot[1]] = 1
    distance[startDot[0]][startDot[1]] = 0
    while queue:
        curN, curM = queue.pop(0)
        for i in range(4):
            newR, newC = curN+dr[i], curM+dc[i]
            # 방문하지 않은 곳이며 동시에 map 범위 안에 있는 곳만 검사합니다.
            if 0<=newR<mapN and 0<=newC<mapM and visited[newR][newC] == 0:
                if mapInfo[newR][newC] == 1:
                    distance[newR][newC] = distance[curN][curM] + 1
                    visited[newR][newC] = 1
                    queue.append([newR, newC])
                # 심지어 여기서 바로 밑의 두 줄을 지워도 
                # 시간이 더 나와요... (41372KB, 788ms)
                # 사실상 위에서 0 처리한 것때문에 없어도 되는 코드인데...
                elif mapInfo[newR][newC] == 0: 
                    distance[newR][newC] = 0

BFS(mapInfo, startDot)

for eachRow in distance:
    print(*eachRow)

'''
중요한 반례
왜냐하면 갈 수 없는 곳이면 아예 0으로 만들어줘야 합니다.
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

'''
#########
# TRYII #
#########
41372KB 728ms
'''

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
        # 위와 동일하지만 미리 0을 설정하는 조건문이 없습니다.
    mapInfo.append(eachRow)

dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

# 위와 동일합니다.
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

# map에서 0인 곳에 결과값이 -1이 나오는 경우 0으로 바꿔주는 처리
for i in range(mapN):
    for j in range(mapM):
        if distance[i][j] == -1 and mapInfo[i][j] == 0:
            distance[i][j] = 0

for eachRow in distance:
    print(*eachRow)
