# https://www.acmicpc.net/problem/18836

from collections import deque
from sys import stdin

Q = deque()

N = int(stdin.readline().strip())

for _ in range(N):
    x = tuple(map(int,stdin.readline().strip().split()))
    if x[0] == 1:
        Q.extendleft([x[1] for _ in range(x[2])])

    elif x[0] == 2:
        Q.extend([x[1] for _ in range(x[2])])

    elif x[0] == 3:
        for _ in range(x[1]):
            Q.popleft()
    elif x[0] == 4:
        for _ in range(x[1]):
            Q.pop()
    elif x[0] == 5:
        print(Q[x[1]-1])
        
'''
2 2 2
3 3 2 2 2
print(3)
3 2 2 2
print(2)
'''