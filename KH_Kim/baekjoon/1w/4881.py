# 백준
# 4881번 : 자리수의 제곱

##* 89, 1
##* 0< a,b < 10^9

#자리수의 제곱을 리스트로 만들기
def makeSquareSum(num):
    numList = [num]   #! [num] 을 list(num)로 하면 에러뜸
    #리스트에 같은 수가 나올 때까지 제곱해서 더하기
    while numList.count(numList[-1]) < 2:  # count() 함수
        calNum = numList[-1]
        newNum = 0
        #숫자를 string으로 변환하여 각 자리에 접근 가능하도록 만들기
        for i in str(calNum):
            newNum += int(i) * int(i)
        numList.append(newNum)
    return numList


#같은 수가 있는지 확인하기
def existSameNum(list01, list02):
    # 각 배열별로 단일 for문을 돌리고, 조건문으로 검색
    minNum = 0
    for i in list01:
        if i in list02:
            minNum = list01.index(i) + list02.index(i) + 2
    for j in list02:
        if j in list01 and minNum > list01.index(j) + list02.index(j)+2:
            minNum = list01.index(j) + list02.index(j) + 2

    return minNum


if __name__ == "__main__":

    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:                               # 둘다 0 이면 종료
            break
        else:
            numListA = makeSquareSum(a)
            numListB = makeSquareSum(b)
            print(a, b, existSameNum(numListA, numListB))   # 출력 ex) 89 89 2
