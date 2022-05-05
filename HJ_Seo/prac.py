# 실험성 코드 페이지입니다. 백준이나 프로그래머스, 앨리스 문제 풀이 파일이 아녜요! - HJ -
#한글문서는 오픈 안됨.

import functools, itertools, random, math, time
import numpy as np #pandas, matplotlib 안깔림 

# 2k + int_(1~n) k/x dx = 3k-k/n
# 2k-k//n-1 ?
# 10 5 3 2 2 1 1 1 1 1 --> 27..
# 10 + int_(1~10) 10/x dx = 10 * ln 10

n = 1000
k = 1300

# # #! test code, 항상 정답이지만 시간 매우 느림.
a = 0
for i in range(1,n+1):
    # print(k%i)
    a += k%i

print('sol =',a)
# # #! ========================================= 
print('============================')
x = int(math.sqrt(k)) # 여기서 x<=n과 n<x case를 구분지어야됨.
# print('x =',x)
c = 0

if k<=n: # done.

    y = 0 
    z = 0

    for i in range(1,x+1):
        c += k//i * i
        c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z # sum k//i + 1 ~ y  = ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2
        y = k//i
        z = i

    c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z

elif x<n:
    
    y = 0 
    z = 0
    for i in range(1,x+1):
        c += k//i * i # 여기는 다 더해줘야함. 왜냐면 x<n이니까. 이후 값은?
        if n >= k//i:
            c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z
        y = min(k//i,n)
        z = i
    
    c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z

else: # n <= x == sqrt(k) .. done
    for i in range(1,n+1):
        c += k//i*i
        
print('my_sol =',n*k - c)



# for i in range(1,x+1):
#     c += k//i * i # done.
#     c += ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2 * z # sum k//i + 1 ~ y  = ( (k//i + 1 + y) * (y - (k//i + 1) + 1) )//2
#     y = k//i
#     z = i
#     # print(y,z)

# c += ( (y + z+1) * (y - (z+1) + 1) )//2 * z





# z = 3 , y = 5 ... sum z + 1 ~ y = ( (y + z+1) * (y - (z+1)) )//2 * z
# 15,15 ==>
# 15 /14 /15 /12 15 !!/12 14 /8 9 10 11 12 13 14 15.

# 20,300 ==> k//i*i
# 300 /300 /300 /300 /300 /300 /294 /296 /297 /300 /297 /300 /299 /294 /300 = 15*20(z,y) /288 = 16*18(z,y) /289 = 17*17(z,y) /! 288 = 18*16 / 285 = 19*15 / 300 = 20*15 .. 

# 5,9 ==>
# 1,9/ 2,4/ 3,3/ 4,2/ 5,1 ... 6,1 7,1 8,1 9,1


# z = int(math.sqrt(k))
# c = 0

# if n <= z:
#     for i in range(1,n+1):
#         c+= k//i*i
#     print(n*k - c)
#     exit(0) # done.

# # sqrt(k) < n case. --> n <= k & k < n
# temp = {}
# for i in range(1,z+1):
#     c += k//i * i
#     temp[i] = k//i

# print('temp =',temp) # done..?
# # n,k = 100,11 case.. temp = {1: 11, 2: 5, 3: 3}
# x = 0 #key
# y = 0 #value

# for key,value in temp.items():
#     c += ((y-value) * (y+value+1))//2 * x
#     x = key
#     y = value
    
#     # print('key,val =',key,v)
#     # print((x - v) , (x + v+1) , y)
#     # c += ((x - v) * (x + v + 1))//2 * y
#     # print('sum =',((x - v) * (x + v + 1))//2 * y)
# #! 낮은 숫자의 n,k에서는 제대로 작동하지 않음. but 큰 수에서는 잘 작동되는게 확인됨.
# print('=================')
# print(n*k - c)

# {18: [1], 9: [2], 6: [3], 4: [4], 3: [5, 6], 2: [7, 8, 9], 1: [10, 11, 12, 13, 14, 15, 16, 17, 18]} ... 33 48 126 ..?
# {15: [1], 7: [2], 5: [3], 3: [4, 5], 2: [6, 7], 1: [8, 9, 10, 11, 12, 13, 14, 15]}
# {5: [1], 2: [2], 1: [3, 4, 5]}
# {3: [1], 1: [2, 3]} 
# 0 1 0 3 3
# --> 3 / 1 1 0 0
#! =================================================================
# x = 15
# dict = {}
# for i in range(1,x+1):
#     if x//i in dict.keys():
#         dict[x//i].append(i)
#     else:
#         dict[x//i] = [i]
        
# print(dict)

# ===================================================================================================

# 17366.

