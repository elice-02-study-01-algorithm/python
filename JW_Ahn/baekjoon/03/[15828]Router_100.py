import sys
from collections import deque

n = int(sys.stdin.readline().strip())
dq = deque()
num = 0

# -1 을 입력받으면 종료
# 길이가 n보다 크다면 그대로 작다면 append 해주기
# 0을 입력받으면 popleft
while True:
    num = int(sys.stdin.readline().strip())
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