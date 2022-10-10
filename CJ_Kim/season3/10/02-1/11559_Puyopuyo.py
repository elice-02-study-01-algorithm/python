import sys
input = sys.stdin.readline
puyoMap = []
for _ in range(12):
    puyoMap.append(list(input().strip()))

# 뿌요지도를 너비 우선 탐색하는데, 같은 색끼리 그룹 묶어서 반환
def BFS(x, y, gameMap):
    BFSvisited=[(x, y)]
    queue = [(x, y)]
    
    while queue:
        dr, dc = [0, 0, 1, -1], [1, -1 ,0, 0]
        currentR, currentC = queue.pop(0)
        for i in range(4):
            newR, newC = currentR + dr[i], currentC + dc[i]
            if 0<=newR<12 and 0<=newC<6:
                if gameMap[newR][newC]==gameMap[x][y] and (newR, newC) not in BFSvisited:
                    BFSvisited.append((newR, newC))
                    queue.append((newR, newC))
    return BFSvisited

# 폭발 연쇄 함수, 뿌요가 4개 붙어있는 것들을 반환
def explosionChain(puyoMap):
    visited = []
    willExploded = []
    for i in range(12):
        for j in range(6):
            if puyoMap[i][j] == '.':
                continue
            if (i, j) in visited:
                continue
            bfsElement = BFS(i, j, puyoMap)
            # append와 extend의 차이
            #[a, b, c] + [d, e] = 
            # append [a, b, c, [d, e]]
            # extend [a, b, c, d, e]
            visited.extend(bfsElement)
            if len(bfsElement) >= 4:
                willExploded.extend(bfsElement)
    return willExploded

# 폭발 예정인 뿌요들을 없애는('.'으로 바꾸기) 함수
def deletePuyos(puyoMap, willExploded):
    # [(1, 3), (2, 5)...]
    for poorPuyo in willExploded:
        r, c = poorPuyo
        puyoMap[r][c] = '.'
    return puyoMap

# 뿌요 폭발 후 뿌요들 떨어뜨리기
# 뿌요는 위에서 아래로 떨어지므로 열끼리 묶어서 처리하는 게 합리적이라고 판단하여,
# 기존 뿌요지도에 2차원 배열에서 행끼리 묶여있는 것을 transpose 하여 역변환한 뒤,
# 열끼리 묶은 곳에서 '.'를 전부 없애고 맨 위에서 12줄만큼 '.'를 채우는 방식
def fallenPuyos(puyoMap):
    transposedMap = []
    for j in range(6):
        tempRow = []
        for i in range(12):
            # '.'가 아니면 새로운 row에 넣어요
            if puyoMap[i][j] != '.':
                tempRow.append(puyoMap[i][j])
        # 여기서 '.'로 꽉 채워요
        while len(tempRow)<12:
            tempRow.insert(0, '.')
        transposedMap.append(tempRow)
    # 다시 역변환한 거를 되돌려줘요
    originMap = []
    for i in range(12):
        tempRow = []
        for j in range(6):
            tempRow.append(transposedMap[j][i])
        originMap.append(tempRow)
    return originMap

chainNum = 0

while True:
    # 폭발 연쇄!
    willExploded = explosionChain(puyoMap)
    # 폭발시킬 게 없네? 그럼 탈출!
    if len(willExploded) == 0:
        break
    # 폭발 시킬 거 다 지워버려!
    deletedPuyoMap = deletePuyos(puyoMap, willExploded)
    # 지웠으면 다 떨어뜨려!
    resultPuyoMap = fallenPuyos(deletedPuyoMap)
    chainNum += 1
    puyoMap = resultPuyoMap

print(chainNum)





