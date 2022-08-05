from itertools import count

row, col = map(int, input().split())

labMap = []
virusInfo = []
possibleWallInfo = []

for i in range(row):
    colInfo = list(map(int, input().split()))
    for j in range(len(colInfo)):
        if colInfo[j] == 2:
            virusInfo.append((i, j))
        elif colInfo[j] == 0:
            possibleWallInfo.append((i, j))
    labMap.append(colInfo)

print(labMap, virusInfo)

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def virusSpread(tempMap, virusList):
    spreadCalMap = tempMap[:]
    while virusList:
        virusR, virusC = virusList.pop(0)
        for i in range(4):
            newR, newC = virusR+dR[i], virusC + dC[i]

            if 0<= newR<row and 0<=newC<col:
                if spreadCalMap[newR][newC] == 0:
                    virusList.append((newR, newC))
                    spreadCalMap[newR][newC] = 2
    return spreadCalMap 

def safeAreaCount(map):
    safeArea = 0
    for row in map:
        safeArea += row.count(0)
    return safeArea

def makeWall(laboratoryMap):
    tempMap = laboratoryMap[:]
    maxSafeArea = 0
    for wall01 in range(len(possibleWallInfo)-2):
        wall01R, wall01C = possibleWallInfo[wall01] 
        for wall02 in range(wall01+1, len(possibleWallInfo)-1):
            wall02R, wall02C = possibleWallInfo[wall02]
            for wall03 in range(wall02+1, len(possibleWallInfo)):
                wall03R, wall03C = possibleWallInfo[wall03]
                
                print('before', tempMap)
                tempMap[wall01R][wall01C] = 1
                tempMap[wall02R][wall02C] = 1
                tempMap[wall03R][wall03C] = 1
                print('after',tempMap)
                print(laboratoryMap)
                spreadMap = virusSpread(tempMap, virusInfo)
                print('spreadMap',spreadMap)
                safeArea = safeAreaCount(spreadMap)
                if maxSafeArea<safeArea:
                    maxSafeArea = safeArea
                print('labMap', labMap)
                tempMap = labMap
            break
        break
    return maxSafeArea

print(makeWall(labMap))