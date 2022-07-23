# https://www.acmicpc.net/problem/1406

# 1차 시도에는 stack을 list로 구현했다가 시간초과가 났습니다.
# deque로 바꾸니 시간초과는 해결했는데, 틀렸습니다가 떠서 
# strip() 및 조건문 수정을 하여 정답처리를 받았습니다.

# global 선언이 있는 경우
# 44640 KB 508 ms
# 없는 경우
# 44668 KB 496 ms

from sys import stdin
from collections import deque
input = stdin.readline

init = input()
order_num = int(input())

# 커서를 기준으로 왼쪽에 있는 것들을 stack1, 오른쪽에 있는 것들을 stack2
stack1 = deque(list(init.strip()))
stack2 = deque([])

def order_operate(letter):
    # 이게 있고 없고 차이가 약 12 ms 정도 납니다
    global stack1, stack2
    if letter == 'L':
        # 커서가 문장의 맨 앞이면 무시됨
        if len(stack1)!=0:
            stack2.appendleft(stack1.pop())
        else:
            return
    elif letter == 'D':
        # 커서가 문장의 맨 뒤이면 무시됨
        if len(stack2)!=0:
            stack1.append(stack2.popleft())
        else:
            return
    elif letter == 'B':
        # 커서가 문장의 맨 앞이면 무시됨
        if len(stack1)!=0:
            stack1.pop()
        else:
            return
    # 'P $'의 경우
    else:
        _, put_letter = letter.split()
        stack1.append(put_letter)

for _ in range(order_num):
    order_operate(input().strip())

print(*(stack1+stack2), sep="")