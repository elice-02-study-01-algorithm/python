# https://www.acmicpc.net/problem/11286
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

operationNum = int(input())

heapQ = []
#[(우선순위, 실제 숫자), (우선순위, 실제 숫자), ...]의 형태로 만듭니다.
# heapQ의 원소들은 우선순위를 바탕으로 정렬됩니다
# 우선순위가 같은 경우 실제 숫자를 비교
# [(1, 1), (2, -2), (2, 2)]

for i in range(operationNum):
    operation = int(input())
    # 0일 경우 가장 작은 수 == 제일 앞에 있는 수 출력
    if operation == 0:
        if heapQ:
            print(heappop(heapQ)[1])
        else:
            print(0)
    # 0이 아닌 경우 양수면 우선순위==실제 숫자, 음수면 우선순위==-(실제 숫자)로 설정하여 heapQ에 넣습니다.
    else:
        if operation < 0:
            heappush(heapQ, (-int(operation), operation))
        else:
            heappush(heapQ, (int(operation), operation))
    
