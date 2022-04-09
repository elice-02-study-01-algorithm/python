import sys
paperSize = int(sys.stdin.readline())

# 전체 색종이 map 그리기
paperMap = []
for _ in range(paperSize):
    rowList = list(map(int, sys.stdin.readline().split()))
    paperMap.append(rowList)

# 1인 종이 세는 변수
global oneCount
oneCount = 0

# 파트별로 나뉜 map의 list를 다시 map화
def makePaperMap(list, paperSize):
    paperMap = []
    index = 0
    paperSize =int(paperSize/2)
    while len(paperMap) <paperSize:
        index += paperSize
        paperMap.append(list[index-paperSize:index])
    return paperMap

# 파트별로 나뉜 list가 더 나눠지는지 확인
def isDividable(part):
    global oneCount
    # 파트의 크기가 4 이상이면 list로 받기 때문에 풀어서 확인해야 함
    print(part)
    if type(part[0]) == list:
        totalValue = []
        for i in part:
            totalValue += i
        if 0 in totalValue and 1 in totalValue:
            return True
        if totalValue.count(1)==len(totalValue):
            oneCount+=1
    # 파트의 크기가 2 이하면 숫자로 받는다.
    # 0과 1이 공존하면 더 나눌 수 있는 것임
    if 0 in part and 1 in part:
        return True

    # 0 또는 1 둘 중 하나만 존재할 때 1의 갯수를 늘린다.
    if part.count(1)==len(part):
        oneCount += 1
    return False


# 리스트 맵으로 받은 것들을 사분면 파트로 나누기
# part01 part02
# part03 part04
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

# 재귀호출을 이용하여 종이 세기
def countPaper(paperMap, paperSize):
    # 끝까지 나눈 경우(종이의 크기가 1인 경우) 1씩 증가
    if paperSize==1:
        if paperMap[0]==1:
            global oneCount
            oneCount += 1
        return 1
    # 전체 파트가 한 가지 숫자로 이루어져 있을 때
    # 가장 처음 검사하는 경우에만 거쳐갈 예정
    if isDividable(paperMap)==False:
        return 1
    # 사분면끼리 나누기
    part01, part02, part03, part04 = partPaper(paperMap, paperSize)
    partMap01=makePaperMap(part01, paperSize)
    partMap02=makePaperMap(part02, paperSize)
    partMap03=makePaperMap(part03, paperSize)
    partMap04=makePaperMap(part04, paperSize)

    # 사분면을 각각 검사하기
    newPaperSize = int(paperSize/2)
    result01 = countPaper(partMap01, newPaperSize if isDividable(part01) else 1)
    result02 = countPaper(partMap02, newPaperSize if isDividable(part02) else 1)
    result03 = countPaper(partMap03, newPaperSize if isDividable(part03) else 1)
    result04 = countPaper(partMap04, newPaperSize if isDividable(part04) else 1)
    result = result01+ result02 + result03 + result04
    return result

# countPaper는 전체 색종이 갯수를 도출함
result = countPaper(paperMap, paperSize)
print(result-oneCount)
print(oneCount)