from sys import stdin

n = int(stdin.readline().strip())
nums = tuple(map(int,stdin.readline().strip().split()))

all_rst = {nums[0]:1}
#초기 결과. 처음에는 수와 그 횟수가 유일함.
temp = dict()
# next_result를 받아줄 dictionary.

for i in range(1,n-1):
    for j in all_rst:
        
        if j - nums[i] >= 0:
            if j - nums[i] not in temp:
                temp[j - nums[i]] = 0
            temp[j - nums[i]] += all_rst[j]
            # 이전 상황에서 all_rst[j] 만큼의 j가 나온 상태. 따라서 j- num[i] 는 all_rst[j]만큼 추가됨.
            
        if j + nums[i] <= 20:
            if j + nums[i] not in temp:
                temp[j + nums[i]] = 0
            temp[j + nums[i]] += all_rst[j]
            #위와 마찬가지.

    all_rst = temp
    # print(all_rst)
    temp = dict()
    
print(all_rst[nums[-1]])