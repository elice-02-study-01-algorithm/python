# from math import sqrt

# A,B = map(int,input().strip().split())

# result = 0

# for i in range(1,A+1):
#     for j in range(1,B+1):
#         if sqrt(i*j)%1 == 0:
#             # print(i,j)
#             result += 1

# print(result)
# print('======================')
# ================================
# from math import sqrt

# N,M = map(int,input().strip().split())

# if N>M:
#     temp = N
#     N = M
#     M = temp

# Prime = [2]

# for i in range(3,M+1):
#     for j in Prime:
#         if i%j == 0:
#             break
        
#     else:
#         Prime.append(i)

# result = 0

# for i in range(1,N+1):
#     c = i
#     if sqrt(i)%1 == 0:
#         M1 = M
#     else:
#         for j in Prime[::-1]:
#             if c%(j**2) == 0:
#                 c = c//(j**2)

#         M1 = M//c
#     print(i,M1)
#     for j in range(1,M1+1):
#         if sqrt(j)%1 == 0:
#             result += 1
    
# print(result)
# ========================
# from math import sqrt

# N,M = map(int,input().strip().split())

# if N>M:
#     temp = N
#     N = M
#     M = temp

# temp = [i for i in range(1,int(sqrt(M))+1)]
# temp2 = set([i**2 for i in range(1,int(sqrt(M))+1)])
# result = 0

# for i in range(1,N+1):
#     c = i
#     for j in temp[::-1]:
#         if c%(j**2) == 0:
#             c = c//(j**2)

#     M1 = M//c
#     # print(i,M1)
#     # for j in range(1,M1+1):
#     #     if j in temp2:
#     #         result += 1
#     result += len(set(range(1,M1+1)) & temp2)
    
# print(result)

# ======================
#! i를 sqruarefree만 남기는 방법은..?
# ! if then, result += M//c....
# 30 30 --> 68
# 100 100 --> 310.
# 1000 1000 --> 4344

from math import sqrt

N,M = map(int,input().strip().split())

if N>M:
    temp = N
    N = M
    M = temp

temp =[i for i in range(1,int(sqrt(M))+1)]
temp2 = set([i**2 for i in range(1,int(sqrt(M))+1)])

result = 0

for i in range(1,N+1):
    c = i
    for j in temp[::-1]:
        if c%(j**2) == 0:
            c = c//(j**2)

    M1 = M//c
    result += len(set(range(1,M1+1)) & temp2)
    
print(result)