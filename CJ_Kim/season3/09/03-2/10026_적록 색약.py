'''
import sys
input = sys.stdin.readline

gridLength = int(input())

colorMap = [[] for _ in range(gridLength)]

for i in range(gridLength):
    rowInfo = list(input().strip())
    colorMap[i] = rowInfo
# [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

unColorBlindness = [[0]*gridLength for _ in range(gridLength)]
colorBlindness = [[0]*gridLength for _ in range(gridLength)]

def BFS(mapInfo):
    queue = [[0, 0]]
    unColorBlindness[0][0] = 1
    colorBlindness[0][0] = 1

    while queue:
        r, c = queue.pop(0)
        curColor = mapInfo[r][c]
        curRegionNumUCB = unColorBlindness[r][c]
        curRegionNumCB = colorBlindness[r][c]

        for i in range(4):
            newR, newC = r+dr[i], c+dc[i]

            if 0<=newR<gridLength and 0<=newC<gridLength and unColorBlindness[newR][newC] == 0 and colorBlindness[newR][newC] == 0:
                nextColor = mapInfo[newR][newC]
                if mapInfo[newR][newC] == curColor:
                    unColorBlindness[newR][newC] = curRegionNumUCB
                    colorBlindness[newR][newC] = curRegionNumCB
                else:
                    unColorBlindness[newR][newC] = curRegionNumUCB + 1
                    if sorted([curColor, nextColor]) == ['G', 'R']:
                        colorBlindness[newR][newC] = curRegionNumCB
                    else:
                        colorBlindness[newR][newC] = curRegionNumCB + 1
                queue.append([newR, newC])


BFS(colorMap)

print(unColorBlindness)
print(colorBlindness)
# [[1, 2, 3, 3, 3], [2, 2, 2, 3, 4], [3, 4, 5, 6, 7], [4, 4, 4, 4, 5], [5, 5, 6, 7, 8]]
# [[1, 1, 2, 2, 2], [2, 2, 2, 3, 3], [3, 3, 3, 3, 3], [4, 4, 4, 4, 5], [5, 5, 5, 6, 7]]
print(max(max(*unColorBlindness)), max(max(*colorBlindness)))



'''


'''

import sys
input = sys.stdin.readline

gridLength = int(input())

colorMap = [[] for _ in range(gridLength)]

for i in range(gridLength):
    rowInfo = list(input().strip())
    colorMap[i] = rowInfo

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

visited = [[0]*gridLength for _ in range(gridLength)]


def BFS(mapInfo):
    unColorBlindnessCount = 1
    colorBlindnessCount = 1
    queue = [[0, 0]]
    visited[0][0] = 1

    while queue:
        r, c = queue.pop(0)
        curColor = mapInfo[r][c]

        for i in range(4):
            newR, newC = r+dr[i], c+dc[i]

            if 0<=newR<gridLength and 0<=newC<gridLength and visited[newR][newC] == 0:
                
                nextColor = mapInfo[newR][newC]
                print('this', nextColor)
                if mapInfo[newR][newC] == curColor:
                    pass
                else:
                    unColorBlindnessCount += 1
                    if sorted([curColor, nextColor]) == ['G', 'R']:
                        pass
                    else:
                        colorBlindnessCount += 1
                visited[newR][newC] = 1
                print(visited, queue)
                queue.append([newR, newC])
    return unColorBlindnessCount, colorBlindnessCount

unCBCount, CBCount = BFS(colorMap)

print(unCBCount, CBCount)


'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

gridLength = int(input())

colorMap = [[] for _ in range(gridLength)]

for i in range(gridLength):
    rowInfo = list(input().strip())
    colorMap[i] = rowInfo
# [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]

'''
1. (0, 0)부터 적록색약이 아닌 경우에 대한 DFS 탐색을 시작합니다.
2. DFS에서 현재 포인트와 다음 탐색 포인트의 색이 같은 경우 탐색을 진행합니다.
   색이 다른 경우, 탐색을 중지합니다.
   탐색한 포인트들은 전부 visited에 넣어줍니다.
3. 이중 for문을 전부 돌면서 visited에 들어가지 않은 곳에 대해 DFS 탐색을 계속해서 진행합니다.
   DFS가 중지될 때마다 구분되는 지역 수(count)에다가 +1을 해줍니다.
4. 적록색약이 아닌 경우 탐색이 끝나면, 이중 for문을 돌며 'G'를 전부 'R'로 바꿔줍니다
5. 1-2-3을 반복합니다.
'''

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def DFS(r, c):
    visited[r][c] = 1
    curColor = colorMap[r][c]
    for i in range(4):
        newR, newC = r+dr[i], c+dc[i]
        if 0<=newR<gridLength and 0<=newC<gridLength and visited[newR][newC] ==0:
            nextColor = colorMap[newR][newC]
            if nextColor == curColor:
                DFS(newR, newC)

def countRegion():
    count = 0
    for i in range(gridLength):
        for j in range(gridLength):
            if (visited[i][j]==0):
                DFS(i, j)
                count +=1
    return count

def makeColorBlind():
    for i in range(gridLength):
        for j in range(gridLength):
            if colorMap[i][j] == 'G':
                colorMap[i][j] = 'R'

visited = [[0]*gridLength for _ in range(gridLength)]
unCBCount = countRegion()

makeColorBlind()

visited = [[0]*gridLength for _ in range(gridLength)]
CBCount = countRegion()

print(unCBCount, CBCount)
