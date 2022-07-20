from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
n = int(input())

for i in range(n):
    instruction = input().split()
    if instruction[0] == 'push_front':
        queue.insert(0,int(instruction[1]))
    elif instruction[0] == 'push_back': 
        queue.append(int(instruction[1]))
    elif instruction[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif instruction[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0) 
    elif instruction[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0]) 
    elif instruction[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])