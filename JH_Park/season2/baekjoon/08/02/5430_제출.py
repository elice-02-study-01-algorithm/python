from collections import deque
from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t):
    p = input()
    n = int(input().rstrip())
    lst = deque(input().rstrip()[1:-1].split(','))
    # 이걸 안 해 주면 deque([''])가 되서 deque이 예외처리가 되지 않아요
    if n == 0:
        lst = deque([])
    isError = False
    isReverse = False
    for case in p:        
        if case == 'R':
            isReverse = not isReverse
        elif case == 'D':
            if lst:
                if isReverse:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                isError = True
                break
    if isError:
        print('error')
    else:
        if isReverse:
            lst.reverse()
            print('['+ ','.join(lst) +']')
        else:
            print('['+ ','.join(lst) +']')