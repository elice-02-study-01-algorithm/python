# https://www.acmicpc.net/problem/17352

# from sys import stdin

# cnt = int(stdin.readline().strip())

# if cnt == 2:
#     print('1 2')
#     exit(0)
    
# grp1 = set()
# tmp = []
# vtx = {i for i in range(1,cnt+1)}

# a,b = map(int,stdin.readline().strip().split())
# grp1.add(a)
# grp1.add(b)
# vtx.discard(a)
# vtx.discard(b)

# for _ in range(cnt-3):
#     a,b = map(int,stdin.readline().strip().split())
#     if a in grp1 or b in grp1:
#         grp1.add(a)
#         grp1.add(b)
#         vtx.discard(a)
#         vtx.discard(b)
    
#     else:
#         tmp.append((a,b))
#         vtx.discard(a)
#         vtx.discard(b)

# if vtx:
#     print(min(grp1),min(vtx))
#     exit(0)

# check = False
# use_idx = {i for i in range(len(tmp))}

# while True:
#     if check == True:
#         break
    
#     check = True
#     del_idx = set()
    
#     for i in use_idx:
#         a,b = tmp[i]
#         if a in grp1 or b in grp1:
#             check = False
#             grp1.add(a)
#             grp1.add(b)
#             del_idx.add(i)
    
#     use_idx -= del_idx

# print(min(grp1),tmp[min(use_idx)][0])

# ! 시간 초과.. 음... 방법이 딱히 생각나지 않는다.. root..?

from sys import stdin

num = int(stdin.readline().strip())
root_one = set()
res = set()
for i in range(num-2):
    a,b = map(int,stdin.readline().strip().split())
    
    if a > b:
        a,b = b,a
    
    if a == 1:
        root_one.add(b)
    elif a in root_one:
        root_one.add(b)
    elif b in root_one:
        root_one.add(a)
    else:
        res.add((a,b))

check_change = True
while True:
    if check_change == False:
        for i in range(2,num+1):
            if i not in root_one:
                print(1,i)
                exit(0)
    
    check_change = False
    for i in range(len(res)):
        x = res.pop()
        if x[0] in root_one:
            root_one.add(x[1])
            check_change = True
            
        elif x[1] in root_one:
            root_one.add(x[0])
            check_change = True
        
        else:
            res.add(x)

# ! 요것도 시간 초과... 음...,,,, 더 좋은 방법이 뭐가 있을까?..;

        