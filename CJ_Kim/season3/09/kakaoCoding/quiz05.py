# update 중 UPDATE, value1, value2의 경우
# 한 값을 다른 한 값으로 갈아끼우기 -> 전체 표를 반환
def updateValue1(cellMap, value1, value2):
    for i in range(51):
        for j in range(51):
            if cellMap[i][j] == value1:
                cellMap[i][j] = value2
    return cellMap

# 전체 표에 대해 BFS 진행 -> merged된 모든 cell의 그룹을 반환
def BFS(mergeInfo, startCell):
    visited = [startCell]
    queue = [startCell]
    while queue:
        currentCell = queue.pop(0)
        for cell in mergeInfo[currentCell]:
            if cell not in visited:
                visited.append(cell)
                queue.append(cell)

    return set(visited)

# update 중 UPDATE, r, c, value의 경우
# merged 된 부분도 UPDATE되야하므로 BFS를 진행해서 바꾼다.
# 전체 표를 반환
def updateMergedValue(cellMap, mergeInfo, r, c, value):

    totalMergedCells = set()
    for keyCell in mergeInfo.keys():
        if keyCell == (r, c):
            totalMergedCells.update(BFS(mergeInfo, (r, c)))
    for mergeCell in totalMergedCells:
        r, c = mergeCell
        cellMap[int(r)][int(c)] = value

    return cellMap

# cell merge시키기 -> 전체 표를 반환
def mergeCell(mergeInfo, cellMap, r1, c1, r2, c2):
    mergedCells = set()
    mergedCells.add((r1, c1))
    mergedCells.add((r2, c2))
    mergedValue = '' 
    
    # 첫 위치로 들어온 것이 비었냐에 따라 merged 값을 다르게 지정하기
    if cellMap[int(r1)][int(c1)] == '':
        if cellMap[int(r2)][int(c2)] == '':
            pass
        else:
            mergedValue = cellMap[int(r2)][int(c2)]
    else:
        mergedValue = cellMap[int(r1)][int(c1)]
        
    # mergedInfo의 key값을 가지고 BFS를 진행하여 전체 mergedCells에 넣기
    for keyCell in mergeInfo.keys():
        if keyCell == (r1, c1):
            mergedCells.update(BFS(mergeInfo, (r1, c1)))

    # mergedCells의 값을 새로운 값으로 업데이트 하기
    for mergeCell in mergedCells:
        r, c = mergeCell
        cellMap[int(r)][int(c)] = mergedValue

    return cellMap

# mergeInfo를 업데이트합니다 -> mergeInfo를 반환
# 일반 그래프 생성하는 것과 동일
def mergeUpdate(mergeInfo, r1, c1, r2, c2):
    # mergedInfo = {(r, c) : [(tempR1, tempC1), (tempR2, tempC2),...]}
    if mergeInfo == {}:
        mergeInfo[(r1, c1)] = [(r2, c2)]
        mergeInfo[(r2, c2)] = [(r1, c1)]
        return mergeInfo

    # merged된 적이 있으면 value에 값만 추가
    for keyCell in mergeInfo.keys():
        if keyCell == (r1, c1):
            mergeInfo[keyCell].append((r2, c2))
        if keyCell == (r2, c2):
            mergeInfo[keyCell].append((r1, c1))

    # merged된 적이 없으면 새로 추가
    if (r1, c1) not in mergeInfo.keys():
        mergeInfo[(r1, c1)] = [(r2, c2)]
    if (r2, c2) not in mergeInfo.keys():
        mergeInfo[(r2, c2)] = [(r1, c1)]
    
    return mergeInfo
            
# unmerge -> 전체 표와 mergeInfo를 반환
def unmergeCell(cellMap, mergeInfo, r, c):
    # r, c로 지정된 셀이 merged된 모든 셀을 구한다
    mergedCells = set()

    for keyCell in mergeInfo.keys():
        if keyCell == (r, c):
            mergedCells.update(BFS(mergeInfo, (r, c)))

    # mergedInfo에서 해당 셀들을 삭제
    for keyCell in mergedCells:
        del mergeInfo[keyCell]
    
    # merged된 적이 없으면 그대로 반환
    if mergedCells == {}:
        return cellMap, mergeInfo

    # 자기 자신은 값이 유지되어야 하므로 추후 작업에서 제외
    if (r, c) in mergedCells:
        mergedCells.remove((r, c))

    # merged된 셀들을 값을 초기화
    for mergeCell in mergedCells:
        r1, c1 = mergeCell
        cellMap[int(r1)][int(c1)] = ''
    
    return cellMap, mergeInfo

def solution(commands):
    cellMap = [['' for _ in range(51)] for _ in range(51)]

    mergeInfo = {}

    answer = []
    for command in commands:
        commandLine = command.split()

        if commandLine[0] == 'UPDATE':
            # [UPDATE, r, c, value]의 경우
            if len(commandLine) == 4:
                r, c, value = commandLine[1:]
                # merged된 적이 있으면
                if (r, c) in mergeInfo.keys():
                    cellMap = updateMergedValue(cellMap, mergeInfo, r, c, value)
                else:
                    cellMap[int(r)][int(c)] = value
            # [UPDATE, value1, value2]의 경우
            else:
                value1, value2 = commandLine[1:]
                cellMap = updateValue1(cellMap, value1, value2)

        elif commandLine[0] == 'MERGE':
            r1, c1, r2, c2 = commandLine[1:]
            # 두 셀을 입력해서 각 셀이 merged된 정보까지 끌어옵니다
            mergeInfo = mergeUpdate(mergeInfo, r1, c1, r2, c2)
            cellMap = mergeCell(mergeInfo, cellMap, r1, c1, r2, c2)

        elif commandLine[0] == 'UNMERGE':
            r, c = commandLine[1:]
            cellMap, mergeInfo = unmergeCell(cellMap, mergeInfo, r, c)

        elif commandLine[0] == 'PRINT':
            r, c = commandLine[1:]
            if cellMap[int(r)][int(c)] == '':
                answer.append("EMPTY")
            else:
                answer.append(cellMap[int(r)][int(c)])

    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))

print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))