# 정수 X에 사용할 수 있는 연산
# 1. X%3 == 0, 3으로 나누기
# 2. X%2 == 0, 2로 나누기
# 3. 1 빼기
# 정수 N이 주어졌을 때 연산 세 개 활용 해 1 만들기
# 연산을 사용하는 횟수의 최솟값

# 입력: 1<N<10**6
# 출력: 첫째 줄에 연산을 하는 횟수의 최솟값
#       둘째 줄에 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해 순서대로 출력
#       정답이 여러가지인 경우 아무거나 출력

'''
N: 입력값
만들 것
1) 연산 횟수를 업데이트하는 리스트
2) resultList = 1~N까지 연산 결과 전부를 업데이트하는 리스트

따로 만든 이유: N번째 줄에서 설명

T[N] 연산 횟수
T[2] = 1 resultList = [0, 0, 1]
T[3] = 1 resultList = [0, 0, 1, 1]
T[4] = 2 resultList = [0, 0, 1, 1, 2]

T[N] 메모이제이션 시작 
기본적으로 <-1 연산>한 것을 저장
    T[N] = T[N-1] + 1
그 다음에 조건문을 돌리는데, 
N%2 == 0 의 경우 <//2 연산>
    T[N-1] + 1 > T[N//2]+1을 만족하면, 최솟값으로 바꿔치기
        T[N] = T[N//2]+1
    resultList도 결과값으로 바꿔치기
N%3 == 0 의 경우 <//3 연산>
    T[N-1] + 1 또는 T[N//2]+1 > T[N//3]+1을 만족하면, 최솟값으로 바꿔치기
        T[N] = T[N//3]+1
    resultList도 결과값으로 바꿔치기
'''

def makeOpList(num):
    opList = [None for _ in range(num+1)]
    resultList = [0 for _ in range(num+1)]
    opList[1] = 0

    for i in range(2, num+1):
        opList[i] = opList[i-1] + 1
        resultList[i] = i - 1
        if i%2 == 0:
            if opList[i]>opList[i//2]+1:
                opList[i] = opList[i//2]+1
                resultList[i] = i//2
        if i%3 == 0:
            if opList[i]> opList[i//3]+1:
                opList[i] = min(opList[i], opList[i//3]+1)
                resultList[i] = i//3
    return opList[num], resultList
    
num = int(input())

answer01, answer02 = makeOpList(num)
print(answer01)

# 메모이제이션 시 전체 범위의 for문을 돌릴 수 밖에 없고,
# 따라서 연산 결과 전부를 업데이트해야한다.
# 그래서 출력할 때 index로 결과값을 접근하여 바로 출력하는 방식을 택함
# index에 해당하는 값이 곧 다음 연산값의 index가 되는 것이 되도록 생성
# ex. N = 10
# resultList = [0, 0, 1, 1, 3, 4, 3, 6, 4, 3, 9] 10(입력 값)
# 출력 순서       ([5])  [4]              [3][2][1] 
# resultList[N] = 9 # 연산 결과이자 다음 연산 결과값을 가진 index

while True:
    print(num, end=" ")
    num = answer02[num]
    if num==0: break