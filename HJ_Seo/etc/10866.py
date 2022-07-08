# 참고!!!

from collections import deque
from sys import stdin

N = int(stdin.readline().strip())

nums = deque()

for _ in range(N):
    arr = stdin.readline().strip()
    
    if arr.startswith('push_front'):
        nums.appendleft(arr[11:])
    if arr.startswith('push_back'):
        nums.append(arr[10:])
    elif arr.startswith('pop_front'):
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.popleft())
    elif arr.startswith('pop_back'):
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.pop())
    elif arr.startswith('size'):
        print(len(nums))
    elif arr.startswith('empty'):
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif arr.startswith('front'):
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[0])
    elif arr.startswith('back'):
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[-1])
            