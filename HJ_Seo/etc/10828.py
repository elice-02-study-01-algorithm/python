from collections import deque
from sys import stdin

N = int(stdin.readline().strip())

nums = deque()

for _ in range(N):
    arr = stdin.readline().strip()
    if arr.startswith('push'):
        nums.append(arr[5:])
    elif arr.startswith('pop'):
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
    elif arr.startswith('top'):
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[-1])