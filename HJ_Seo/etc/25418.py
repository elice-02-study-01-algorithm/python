# https://www.acmicpc.net/problem/25418
# 제한 1 ≤ A < K ≤ 1,000,000

# start,end = map(int,input().split())

# current = {start}
# done = set()
# num = 1

# while True:
#     next = set()
#     for i in current:
#         x = i+1
#         if x not in done:
#             next.add(x)
#             done.add(x)
        
#         x = 2*i
#         if x not in done:
#             next.add(x)
#             done.add(x)
    
#     if end in next:
#         print(num)
#         exit()
    
#     current = next
#     num += 1

# ! 안봐도 비디오인 시간초과.

start,end = map(int,input().split())

dep = [None for _ in range(end+1)]

dep[start] = 0
num = 1
tmp = {start}

while True:
    if dep[-1] != None:
        print(dep[-1])
        break
    
    tmp2 = set()
    
    for i in tmp:
        if i+1<=end and dep[i+1] == None:
            dep[i+1] = num
            tmp2.add(i+1)
        
        if 2*i<=end and dep[2*i] == None:
            dep[2*i] = num
            tmp2.add(2*i)
    
    # if len(tmp2) == 0:
    #     print(tmp)
    #     break   # !  check용
    
    tmp = tmp2
    num += 1
