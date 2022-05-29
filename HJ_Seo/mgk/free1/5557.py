from sys import stdin

n = int(stdin.readline().strip())
nums = tuple(map(int,stdin.readline().strip().split()))
# print(n,nums)
all_rst = {nums[0]:1}
temp = dict()

for i in range(1,n-1):
    for j in all_rst:
        
        if j - nums[i] >= 0:
            if j - nums[i] not in temp:
                temp[j - nums[i]] = 0
            temp[j - nums[i]] += all_rst[j]
            
        if j + nums[i] <= 20:
            if j + nums[i] not in temp:
                temp[j + nums[i]] = 0
            temp[j + nums[i]] += all_rst[j]

    all_rst = temp
    # print(all_rst)
    temp = dict()
    
print(all_rst[nums[-1]])