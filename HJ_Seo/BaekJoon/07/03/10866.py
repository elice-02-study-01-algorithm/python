from collections import deque
from sys import stdin

N = int(stdin.readline().strip())

nums = deque()

for _ in range(N):
    arr = stdin.readline().strip()
    
    if arr.startswith('push_front'):
        nums.appendleft(arr[11:])
    elif arr.startswith('push_back'):
        nums.append(arr[10:])
    elif arr.startswith('pop_front'):
        print(-1 if len(nums) == 0 else nums.popleft())
    elif arr.startswith('pop_back'):
        print(-1 if len(nums) == 0 else nums.pop())
    elif arr.startswith('size'):
        print(len(nums))
    elif arr.startswith('empty'):
        print(1 if len(nums) == 0 else 0)
    elif arr.startswith('front'):
        print(-1 if len(nums) == 0 else nums[0])
    elif arr.startswith('back'):
        print(-1 if len(nums) == 0 else nums[-1])
