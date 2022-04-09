## 백준
## 4256번 : 트리
## 트리, 분할 정복, 재귀
##* 전위, 중위 순회 결과를 가지고 후위 순회 구하는 프로그램

## 풀이 접근 방법
## 전위의 제일 처음은 루트이다
## 루트를 통해서 중위에서 Left와 right를 나눌 수 있다
## 이러한 방식을 재귀를 통해서 반복하여 루트, L, R를 분할하여 후위를 완성

import sys


def findIndex(preO, inO):
    ##* 재귀 종료
    if len(preO) == 0:
        return
    elif len(preO) == 1:
        print(preO[0], end=' ')
        return
    elif len(preO) == 2:
        print(preO[1], preO[0], end=' ')
        return
    
    root = preO[0]

    midIndex = inO.index(root)      # 4
    # print('mid!!!!',midIndex)
    ##* 분할

    # 중위 divide 부분
    inOLeft = inO[:midIndex]        # 0~3
    inORight = inO[midIndex+1:]     # 5~7
    # 전위 divide 부분
    preOLeft = preO[1:midIndex+1]   # 1~4
    preORight = preO[midIndex+1:]   # 5~7

    ##* 재귀
    findIndex(preOLeft, inOLeft)
    findIndex(preORight, inORight)

    print(root, end=' ')

    '''
    postOrder = [0 for i in range(n)]   ## 길이가 n인 0 리스트

    data_join = ' '.join(postO)         ## 리스트 join함수 사용 변환
    print(data_join)

    '''


if __name__ == '__main__':
    T = int(input())  # Test case

    for i in range(T):
        n = int(input())  # 노드수
        preO = list(map(int, sys.stdin.readline().split()))
        inO = list(map(int, sys.stdin.readline().split()))

        findIndex(preO, inO)
        print()
