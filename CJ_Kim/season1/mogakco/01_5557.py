'''
[1학년](https://www.acmicpc.net/problem/5557)
'''
'''
음수 X, 20을 넘는 수는 모른다
중간에 나오는 수가 모두 0 이상 20 이하
만들 수 있는 등식의 개수

T(N) = T(N-1) 
Sum = [None, 1, / 11, 10 / 110, 111, 100, 101 / ]
이진 트리를 이용할 수도 있지 않을까 했지만 가장 깊은 노드들의 수를 더하는 방법을 몰라서 pass
'''
import sys
input = sys.stdin.readline

numN = int(input())
numList = list(map(int, input().split()))

def makeOp(numN):
    # {1:[0]*21, 2:[0]*21, ..., numN-1:[0]*21}인 딕셔너리 생성
    sumDic = {}
    for i in range(1, numN):
        sumDic[i] = [0]*21

    # 첫번째 수가 인덱스인 곳에 +1 (한 가지 방법뿐이므로)
    # 즉 첫번째 연산(==sumDic[1])에서 만들 수 있는 경우의 수는 
    # 각 인덱스 값, 해당 인덱스는 연산 결과
    sumDic[1][numList[0]] = 1

    # 이전 회차 키 값의 벨류인 리스트에 경우의 수가 있으면 
    # 해당 경우의 수에다가 현재 인덱스를 결과값으로 가지는 곳에 더하기
    for i in range(2, numN):
        for j in range(21):
            if sumDic[i-1][j] == 0:
                continue
            if j+numList[i-1] <= 20:
                sumDic[i][j+numList[i-1]] += sumDic[i-1][j]
            if j-numList[i-1] >= 0:
                sumDic[i][j-numList[i-1]] += sumDic[i-1][j]
    return sumDic[numN-1][numList[-1]]

print(makeOp(numN))



