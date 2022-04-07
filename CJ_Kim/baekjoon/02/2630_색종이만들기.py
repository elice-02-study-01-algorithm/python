import sys
paperSize = int(sys.stdin.readline())

paperMap = []
for _ in range(paperSize):
    rowList = list(map(int, sys.stdin.readline().split()))
    paperMap.append(rowList)

global oneCount
oneCount = 0

def makePaperMap(list, paperSize):
    paperMap = []
    index = 0
    paperSize =int(paperSize/2)
    while len(paperMap) <paperSize:
        index += paperSize
        paperMap.append(list[index-paperSize:index])
    return paperMap

def isDividable(part):
    global oneCount
    if type(part[0]) == list:
        totalValue = []
        for i in part:
            totalValue += i
        if 0 in totalValue and 1 in totalValue:
            return True
        if totalValue.count(1)==len(totalValue):
            oneCount+=1
    if 0 in part and 1 in part:
        return True
    if part.count(1)==len(part):
        oneCount += 1
    return False



def partPaper(paperMap, paperSize):
    searchList01 = [i for i in range(0, int(paperSize/2))]
    searchList02 = [j for j in range(int(paperSize/2), paperSize)]

    part01 = []
    part02 = []
    part03 = []
    part04 = []
    for i in range(paperSize):
        for j in range(paperSize):
            if i in searchList01 and j in searchList01:
                part01.append(paperMap[i][j])
            elif i in searchList02 and j in searchList01:
                part03.append(paperMap[i][j])
            elif i in searchList01 and j in searchList02:
                part02.append(paperMap[i][j])
            else:
                part04.append(paperMap[i][j])
    return [part01, part02, part03, part04]


def countPaper(paperMap, paperSize):
    if paperSize==1:
        if paperMap[0]==1:
            global oneCount
            oneCount += 1

        return 1
    if isDividable(paperMap)==False:
        return 1
    part01, part02, part03, part04 = partPaper(paperMap, paperSize)
    newPaperSize = int(paperSize)
    partMap01=makePaperMap(part01, newPaperSize)
    partMap02=makePaperMap(part02, newPaperSize)
    partMap03=makePaperMap(part03, newPaperSize)
    partMap04=makePaperMap(part04, newPaperSize)

    newPaperSize = int(paperSize/2)
    result01 = countPaper(partMap01, newPaperSize if isDividable(part01) else 1)
    result02 = countPaper(partMap02, newPaperSize if isDividable(part02) else 1)
    result03 = countPaper(partMap03, newPaperSize if isDividable(part03) else 1)
    result04 = countPaper(partMap04, newPaperSize if isDividable(part04) else 1)
    result = result01+ result02 + result03 + result04
    return result

#print(countPaper([[1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], 4))
# print(countPaper(paperMap, paperSize))
# print(oneCount)
# print(countPaper(paperMap, paperSize)-oneCount)
# print(countPaper(paperMap, paperSize))
result = countPaper(paperMap, paperSize)
print(result-oneCount)
print(oneCount)