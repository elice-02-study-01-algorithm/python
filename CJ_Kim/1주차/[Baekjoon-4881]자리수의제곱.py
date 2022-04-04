def makeSquareSum(num):
    numList = [num]
    while numList.count(numList[-1]) <2:
        calNum = numList[-1]
        if calNum <10:
            numList.append(calNum**2)
        else:
            newNum = 0
            for i in str(calNum):
                newNum += int(i)**2
            numList.append(newNum)
    return numList

def existSameNum(list01, list02):
    minNum = 0
    for i in range(len(list01)):
        for j in range(len(list02)):
            if list01[i] == list02[j]:
                minNum = i+j+2
    for j in range(len(list02)):
        for i in range(len(list01)):
            if list01[i] == list02[j]:
                if minNum > i+j+2:
                    minNum = i+j+2

    return minNum

while True:
    numA, numB = map(int, input().split())
    if numA == 0 and numB == 0:
        break
    else:
        numList01 = makeSquareSum(numA)
        numList02 = makeSquareSum(numB)
        print(numA, numB, existSameNum(numList01, numList02))
        