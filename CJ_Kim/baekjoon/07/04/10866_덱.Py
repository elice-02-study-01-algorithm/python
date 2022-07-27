#############
### 풀이 I ###
#############
# 32508 KB 224 ms
# class를 이용
# exec()가 핵심 [참고](https://mindcompass.github.io/programming/programming(python)/)
'''
from collections import deque
import sys
input = sys.stdin.readline

order_num = int(input())

class Deq:
    
    def __init__(self):
        self.deque01 = deque()
    
    def push_front(self, number):
        self.deque01.appendleft(number)

    def push_back(self, number):
        self.deque01.append(number)

    def isEmpty(self):
        if len(self.deque01) == 0:
            return 1
        else: return 0

    def empty(self):
        if self.isEmpty() == 1:
            print(1)
        else:
            print(0)

    def size(self):
        print(len(self.deque01))
    
    def pop_front(self):
        if self.isEmpty() == 1:
            print(-1)
        else:
            print(self.deque01.popleft())
    
    def pop_back(self):
        if self.isEmpty() == 1:
            print(-1)
        else:
            print(self.deque01.pop())
    
    def front(self):
        if self.isEmpty() == 1:
            print(-1)
        else:
            print(self.deque01[0])
    
    def back(self):
        if self.isEmpty() == 1:
            print(-1)
        else:
            print(self.deque01[-1])

dequeAnswer = Deq()

for _ in range(order_num):
    order = input().strip()
    if order[:4] == 'push':
        order_op, number = order.split()
        execute = 'dequeAnswer.{0}({1})' .format(order_op, number)
        exec(execute)
    else:
        order_op = order
        execute = 'dequeAnswer.{0}()' .format(order_op)
        exec(execute)
'''
#############
### 풀이 II ##
#############
# 32452 KB 96 ms
# 조건문을 이용
from collections import deque

# ⭐️⭐️⭐️readline을 쓰지 않으면 시간 초과가 납니다 매우 중요⭐️⭐️⭐️
import sys
input = sys.stdin.readline

order_num = int(input())

deque01 = deque()

for _ in range(order_num):
    order = input().strip()
    if order[:4] == 'push':
        order_op, number = order.split()
    else:
        order_op = order
    if order_op == 'push_back':
        deque01.append(number)
    elif order_op == 'push_front':
        deque01.appendleft(number)
    elif order_op == 'pop_front':
        print(deque01.popleft()) if deque01 else print(-1)
    elif order_op == 'pop_back':
        print(deque01.pop()) if deque01 else print(-1)
    elif order_op == 'size':
        print(len(deque01))
    elif order_op == 'empty':
        print(0) if deque01 else print(1)
    elif order_op == 'front':
        print(deque01[0]) if deque01 else print(-1)
    else:
        print(deque01[-1]) if deque01 else print(-1)
