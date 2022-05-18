from collections import deque

n = int(input())
dq = deque()
num = 0

while True:
    num = int(input())
    if num == -1:
        break
    if num == 0:
        dq.popleft()
    elif len(dq) < n:
        dq.append(num)
    
if dq:
    print(*dq)
else:
    print("empty")