case = int(input())
for i in range(case):
    n = int(input())
    
    dic = {}
    for i in range(n):
        x,y = map(str,input().strip().split())
        if y not in dic:
            dic[y] = 0
        dic[y] += 1
    
    nums = tuple(dic.values())
    
    result = 1
    for i in range(len(nums)):
        result *= (nums[i]+1)
    
    print(result - 1)
