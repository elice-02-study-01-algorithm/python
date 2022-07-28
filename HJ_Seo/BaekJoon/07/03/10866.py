from collections import deque
from sys import stdin

N = int(stdin.readline().strip())

nums = deque()

# 이전에 푼거.. 개선사항은 if else문 개선..?.. 예전꺼랑 비교해서 시간 차이는 없지만 메모리는 10kb정도? 줄더라..ㅎㅎ..
for _ in range(N):
    arr = stdin.readline().strip() # 슬라이싱이 좀 더 빠르다는 의견!
    
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
