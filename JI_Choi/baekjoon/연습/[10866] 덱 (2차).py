from sys import stdin
from collections import deque

# n 입력받기
n = int(stdin.readline())
q = deque()

for _ in range(n):
    info = stdin.readline().strip()
    # pop_front
    if info == 'pop_front':
        if len(q) == 0:
            print('-1')
        else:
            print(q.popleft())
    # pop_back
    elif info == 'pop_back':
        if len(q) == 0:
            print('-1')
        else:
            print(q.pop())
    # size
    elif info == 'size':
        print(len(q))
    # empty
    elif info == 'empty':
        if len(q) == 0:
            print('1')
        else:
            print('0')
    # front
    elif info == 'front':
        if len(q) == 0:
            print('-1')
        else:
            e = q.popleft()
            print(e)
            q.appendleft(e)
    # back
    elif info == 'back':
        if len(q) == 0:
            print('-1')
        else:
            e = q.pop()
            print(e)
            q.append(e)
    # push_front
    elif 'push_front' in info:
        q.appendleft(info[11:])
    # push_back
    else:
        q.append(info[10:])
    
