#자리수의 제곱을 리스트로 만들기
def makeSquareSum(num):
    numList = [num]
    #리스트에 같은 수가 나올 때까지 제곱해서 더하기
    while numList.count(numList[-1]) <2:
        calNum = numList[-1]
        newNum = 0
        #숫자를 string으로 변환하여 각 자리에 접근 가능하도록 만들기
        for i in str(calNum):
            newNum += int(i)**2
        numList.append(newNum)
    return numList

#같은 수가 있는지 확인하기
def existSameNum(list01, list02):
    # 방법 1. 각 배열별로 이중 for문을 돌려 있는지 확인(320ms)
    # minNum = 0
    # for i in range(len(list01)):
    #     for j in range(len(list02)):
    #         if list01[i] == list02[j]:
    #             minNum = i+j+2
    # for j in range(len(list02)):
    #     for i in range(len(list01)):
    #         if list01[i] == list02[j]:
    #             if minNum > i+j+2:
    #                 minNum = i+j+2

    # 방법 2. 각 배열별로 단일 for문을 돌리고, 조건문으로 검색(304ms)
    # 시간이 방법 1.보다 다소 줄었음
    minNum = 0
    for i in list01:
        if i in list02:
            minNum = list01.index(i) + list02.index(i) +2
    for j in list02:
        if j in list01 and minNum>list01.index(j) + list02.index(j)+2:
            minNum = list01.index(j) + list02.index(j) +2

    return minNum

while True:
    numA, numB = map(int, input().split())
    if numA == 0 and numB == 0:
        break
    else:
        numList01 = makeSquareSum(numA)
        numList02 = makeSquareSum(numB)
        print(numA, numB, existSameNum(numList01, numList02))
        