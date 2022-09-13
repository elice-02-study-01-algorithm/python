'''
import sys
input = sys.stdin.readline

def calculate(revenueList):
    tempMax = max(revenueList)
    tempSum = 0
    index = 0

    if len(revenueList) <= 3:
        return max(tempMax, sum(revenueList))

    if revenueList[0] > 0:
        index = 0
        tempSum = revenueList[index]
    else:
        index = 1
        tempSum = revenueList[index]
    
    for currentIndex in range(index+1, len(revenueList)):
        if currentIndex+1 > len(revenueList)-1:
            break
        tempSum = tempSum + revenueList[currentIndex] + revenueList[currentIndex+1]
        if tempSum > tempMax:
            tempMax = tempSum
    return tempMax


def shorten(count):
    ifNegativeList = []
    revenueList = []
    wasNegative = False
    isNegative = False
    tempSum = 0
    for i in range(count):
        todayRevenue = int(input())

        wasNegative = isNegative
        isNegative = todayRevenue < 0

        if ifNegativeList != [0]:
            if isNegative:
                ifNegativeList.append(todayRevenue)
            else:
                ifNegativeList = [0]

        if i == 0:
            tempSum += todayRevenue
            continue

        if wasNegative != isNegative:
            revenueList.append(tempSum)
            tempSum = todayRevenue
        else:
            tempSum += todayRevenue

    revenueList.append(tempSum)

    if len(ifNegativeList) == count:
        return ifNegativeList

    return revenueList

while True:
    testCaseCount = int(input())
    if testCaseCount == 0:
        exit()
    shortenList = shorten(testCaseCount)
    if max(shortenList) <0:
        print(max(shortenList))
    else:
        print(calculate(shortenList))

'''
'''
import sys
input = sys.stdin.readline

def shorten(count):
    stack = []
    isAllNegative = True
    negativeList = []
    for i in range(count):

        todayRevenue = int(input())

        isAllNegative = todayRevenue < 0
        isNegative = todayRevenue < 0

        if not isAllNegative:
            pass
        else:
            negativeList.append(todayRevenue)

        if i == 0:
            stack.append(todayRevenue)
            continue
        
        if stack[-1] < 0:
            if isNegative:
                stack[-1] += todayRevenue
            else:
                stack.append(todayRevenue)
        else:
            if isNegative:
                stack.append(todayRevenue)
            else:
                stack[-1] += todayRevenue

    if len(negativeList) == count:
        return negativeList
        # [-1000, -19]

    return stack
    # [-3, 13, -7, 8]

def sumMax(revenueList):
    tempMax = max(revenueList)
    
    revenueList = revenueList + [0, 0]
    answerStack = []

    if revenueList[0] < 0:
        revenueList.pop(0)
    length = len(revenueList) -2
    print('list', revenueList)
    for i in range(1, length, 2): 
        print(revenueList[i-1], revenueList[i+1], revenueList[i])
        if i == length-1 or i == length:
            answerStack.append(revenueList[i-1])
            break
        
        if revenueList[i-1] + revenueList[i+1] > abs(revenueList[i]):
            answerStack.append(revenueList[i-1] + revenueList[i])
    print(answerStack)

    return max(tempMax, sum(answerStack))
            # [ 2 -18 8 -29 8 -1 19 -3]

while True:
    testCaseCount = int(input())
    if testCaseCount == 0:
        exit()
    shortenList = shorten(testCaseCount)
    if max(shortenList) < 0:
        print(max(shortenList))
    else:
        print(sumMax(shortenList))

# 도저히 반례를 못 찾겠어..
# [2, -1, 3, -1] - 3이 나와 이건 해결 완료 


# 드디어 풀었습니다!!!
# 47116KB ⭐️720ms⭐️

'''
import sys
input = sys.stdin.readline

# 양수는 양수끼리, 음수는 음수끼리 묶어서 미리 더해버리기
def shorten(count):
    stack = []
    isAllNegative = True
    negativeList = []

    for i in range(count):
        todayRevenue = int(input())

        isAllNegative = todayRevenue < 0
        isNegative = todayRevenue < 0

        # 모든 수익이 음수인 경우(왜 사업을 안 접는지 의문)
        # 합치면 안되므로 한 곳에 미리 저장해두기
        if not isAllNegative:
            pass
        else:
            negativeList.append(todayRevenue)

        # 처음에는 넣기만 하기
        if i == 0:
            stack.append(todayRevenue)
            continue
        
        # 이전의 것과 현재의 것의 음양을 비교해 넣기
        if stack[-1] < 0:
            if isNegative:
                stack[-1] += todayRevenue
            else:
                stack.append(todayRevenue)
        else:
            if isNegative:
                stack.append(todayRevenue)
            else:
                stack[-1] += todayRevenue
    
    # 음수만 있는 경우
    if len(negativeList) == count:
        return negativeList

    return stack

while True:
    testCaseCount = int(input())

    if testCaseCount == 0:
        exit()
    
    # 수익들 음양으로 묶어서 압축시키기
    shortenList = shorten(testCaseCount)

    # 음수만 있는 경우
    if max(shortenList) < 0:
        print(max(shortenList))
    else:
        # 압축시킨 수열로다가 DP 처리 하기
        for i in range(1, len(shortenList)):
            if shortenList[i-1] + shortenList[i] > shortenList[i]:
                shortenList[i] = shortenList[i-1] + shortenList[i]
        print(max(shortenList))