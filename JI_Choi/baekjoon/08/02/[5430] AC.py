from collections import deque
from sys import stdin
input = stdin.readline

# 테스트 케이스의 개수 입력받기
t = int(input())

# 테스트 케이스의 개수만큼 반복
for i in range(t):
    # 수행할 함수 입력받기
    p = input().strip()
    # 배열의 크기 입력받기
    n = int(input())
    # (배열 형태의)문자열을 배열로 변환하여 입력받기
    arr = input().strip()
    # 입력된 arr 값이 '[]'인 경우
    if arr == '[]':
        # 문자열을 배열로 변환
        arr = []
    # 입력된 arr 값이 '[]' 이외의 값인 경우
    else:
        # 문자열을 배열로 변환
        arr = arr.replace('[','').replace(']','').split(",")
    # 방향에 대한 정보 저장 (1: 정방향, -1:역방향)
    reverse = 1
    # 트리거 선언
    trigger = 0
    # deque 선언
    deq = deque(arr)

    # 수행할 함수에 각각 접근
    for i in p:
        
        # 함수가 'R'인 경우
        if i == 'R':
            reverse *= -1

        # 함수가 "D"인 경우
        elif i == 'D':
            # deque에 원소가 존재하지 않는 경우
            if len(deq) == 0:
                # error 출력
                print('error')
                trigger = 1
                break
            # deque에 원소가 존재하는 경우
            else:
                if reverse == 1:
                    deq.popleft()
                else:
                    deq.pop()

    # trigger가 0인 경우 (즉, error를 출력하지 않은 경우)
    if trigger == 0:
        # reverse가 1인 경우
        if reverse == 1:
            # 배열을 문자열로 변환
            print('['+','.join(list(deq))+']')
        else:
            answer = list(deq)
            # 배열을 역순으로 정렬
            answer.reverse()
            # 배열을 문자열로 변환
            print('['+','.join(answer)+']')