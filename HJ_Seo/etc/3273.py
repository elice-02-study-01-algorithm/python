# from sys import stdin

# leng = int(stdin.readline().strip())
# nums = tuple(map(int,stdin.readline().strip().split()))
# aim = int(stdin.readline().strip())
# cnt = 0

# if aim%2 == 1:
#     for i in range(leng):
#         cnt += nums.count(aim-nums[i])
# else:    
#     for i in range(leng):
#         if nums[i] == aim//2:
#             cnt += nums.count(nums[i])/2
#         else:
#             cnt += nums.count(aim-nums[i])
    
# print(int(cnt)//2)

# ! 시간초과..?.. 아 n 갯수.. count사용한 것도 시간 초과..?..

from sys import stdin

leng = int(stdin.readline().strip())
nums = sorted(map(int,stdin.readline().strip().split()))
aim = int(stdin.readline().strip())
cnt = 0

left,right = 0, leng-1

while left != right:
    if nums[left]+nums[right]==aim:
        cnt += 1
        left += 1
    elif nums[left] + nums[right] < aim:
        left += 1
    else:
        right -= 1

print(cnt)