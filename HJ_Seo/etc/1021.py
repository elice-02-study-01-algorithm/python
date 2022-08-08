from sys import stdin
from collections import deque

def sec_proc(Q,n):
    for _ in range(n):
        Q.append(Q.popleft())
    
def thr_proc(Q,n):
    for _ in range(n):
        Q.appendleft(Q.pop())

N,M = map(int,stdin.readline().strip().split())
cnt = 0
nums = tuple(map(int,stdin.readline().strip().split()))
idx = 0

Q = deque()
for i in range(1,N+1):
    Q.append(i)

for _ in range(M):
    left = Q.index(nums[idx])
    right = len(Q)-left
    if right>=left:
        cnt += left
        sec_proc(Q,left)
    else:
        cnt += right
        thr_proc(Q,right)
    Q.popleft()
    
    idx += 1

print(cnt)