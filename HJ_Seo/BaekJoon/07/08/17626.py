# https://www.acmicpc.net/problem/17626

# from itertools import combinations_with_replacement as cr

# import time

# init_time = time.time()

# num = int(input())
# tmp = 1
# sqr = []
# while tmp**2<=num:
#     sqr.append(tmp**2)
#     tmp += 1

# for i in range(1,6):
#     for j in cr(sqr,i):
#         if sum(j) == num:
#             print(len(j))
#             print(time.time()-init_time)
#             exit(0)

# ! 시간초과 뜨네..,,ㅎㅎ,,

# import time

# init_time = time.time()

# num = int(input())
# tmp = 1
# sqr = []
# while tmp**2<=num:
#     sqr.append(tmp**2)
#     tmp += 1

# cnts = [0 for _ in range(num+1)]
# for i in sqr:
#     cnts[i] = 1

# use_idx = set(sqr)

# while True:
#     if cnts[num] != 0:
#         print(cnts[num])
#         break
    
#     next_idx = set()
#     for i in use_idx:
#         for j in sqr:
#             x = i+j
#             if x<=num and cnts[x] == 0:
#                 cnts[x] = cnts[i] + 1
#                 next_idx.add(x)
#             elif x>num:
#                 continue
    
#     use_idx = next_idx
                
# print(time.time() - init_time)

# ! 두 번째보다 시간이 오래 걸림...,,,

from itertools import combinations_with_replacement as cr

num = int(input())
tmp = 1
sqr = []
while tmp**2<=num:
    sqr.append(tmp**2)
    tmp += 1

if num == sqr[-1]:
    print(1)
    exit(0)

for i in range(2,4):
    for j in cr(sqr,i):
        if sum(j) == num:
            print(i)
            exit(0)

print(4)  # 2도 아니고 3도 아니면 갯수는 무조껀 4겠지..

# ! Clear.. 아래 코드는 더 좋은 코드.

# def check(num):
#     sqr = num**(0.5)
#     if sqr.is_integer():
#         print(1)
#         return 
    
#     for i in range(1,int(sqr)+1):
#         if ((num-i*i)**(0.5)).is_integer():
#             print(2)
#             return
    
#     for i in range(1,int(sqr)+1):
#         for j in range(i,int(sqr)+1):
#                 res = (num - i*i - j*j)
#                 if res<=0:
#                     continue
                
#                 if (res**(0.5)).is_integer():
#                     print(3)
#                     return
    
#     print(4)
#     return
    
# check(int(input()))
