# 백준
# 15828번 : Router
## 자료구조, 큐

# * 문제 규칙
# 버퍼 buffer 의 상태 변화
# 입력1 : 버퍼의 크기를 나타내는 자연수 N
# 입력~ : 라우터가 처리해야할 정보
# 0 : 라우터가 패킷 하나 처리
# -1 : 입력의 끝
# 버퍼 비어있을 때 empty 출력

import sys
from collections import deque


def router(n, data):
    queue = deque()
    for i in range(len(data)):
        # 0인경우 pop
        if data[i] == [0]:
            queue.popleft()
        # 버퍼 크기 여유있으면 큐에 append
        elif len(queue) <= n-1:
            queue.append(data[i])
    return queue


if __name__ == '__main__':
    N = int(input())
    data = []
    end = 1
    while (end != [-1]):
        data.append(list(map(int, sys.stdin.readline().split())))
        end = data[-1]

    # -1 제거
    data.pop()

    result = router(N, data)
    if len(result) == 0:
        print('empyty')
    else:
        for i in range(len(result)):
            # 데이터가 리스트 타입이여서 숫자 출력시 0번 인덱스로 접근
            print(result[i][0], end=" ")
