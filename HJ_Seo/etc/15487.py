# A[j]-A[i]+A[l]-A[k]
'''
원하는거..
작,크,작,크 순서중에 재일 양질의 수.

'''

'''
# # test용
# import time
# import random

# n = 300
# nums = []
# for i in range(300):
#     nums.append(random.randint(1,10000))

# print(n,nums)
'''

# from sys import stdin
# from math import inf
# n = int(stdin.readline())
# nums = list(map(int,stdin.readline().strip().split()))

# start_time = time.time()  #####################################
# def getMax(lst):
#     result = -inf
#     for i in range(0,len(lst)-1):
#         for j in range(i+1,len(lst)):
#             result = max(result,lst[j]-lst[i])
            
#     return result

# result = -inf
# for i in range(1,n-1):
#     front = getMax(nums[:i])
#     back = getMax(nums[i:])
#     result = max(result,front + back)

# print(result)
# print('case1 =',time.time()-start_time)
#100만개의 숫자가 들어가있는 케이스가 시간초과..,,
# default code.


# from sys import stdin
# from math import inf

# def getMax2(lst,n):

#     def getMax(start,end):
#         result = -inf
#         for i in range(start,end-1):
#             for j in range(i+1,end):
#                 result = max(result,lst[j]-lst[i])
                
#         return result

#     result = -inf
#     lst = tuple(lst)
#     front_max = lst[1]
#     front_min = lst[0]
#     check_max_ord = 1
#     check_min = [lst[0],0]

#     for i in range(2,n-1):
#         back = getMax(i,n)
#         # print('back = ',back)
#         # print('front =',front_max - front_min)
#         if min(front_min,check_min[0]) >= lst[i-1]:
#             check_min = [lst[i-1],i-1]

#         if front_max <= lst[i-1] and check_min[1]<i-1:
#             front_max = lst[i-1]
#             check_max_ord = i-1
#             if check_max_ord > check_min[1]:
#                 front_min = check_min[0]

#         result = max(result,front_max-front_min + back)

#     return result

# n = int(stdin.readline())
# nums = map(int,stdin.readline().strip().split())

# '''
# # start_time = time.time() ###################################################################
# '''

# result = getMax2(nums,n)

# print(result)
# '''
# print('case2 =',time.time()-start_time)  ##############################################################
# '''
# 마찬가지로 시간초과.. getMax가 문제인듯..  재일 빠르긴 함..
# 200개 기준 0.7초, 300개만 되어도 2.6초가 걸림.


# from sys import stdin
# from math import inf

# n = int(stdin.readline())
# nums = tuple(map(int,stdin.readline().strip().split()))

# start_time = time.time()  ###################################################

# result = -inf
# for i in range(1,n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             b = min(nums[:i])
#             a = max(nums[i:j])
#             d = min(nums[j:k])
#             c = max(nums[k:])
#             result = max(result,a-b+c-d)

# print(result)
# print('case3 =',time.time()-start_time)
# 가장 무식한 방법..  물론 결과는 나오지만 시간은??  100개기준 case1의 3배..X

# ====================================================================================================
#case_divide_prob..  max와 min을 구하는 것 자체는 시간이 엄청 짧게 걸림.(길이 100만개짜리 list 기준으로 합해서 0.01초?, 
# index를 통해 정보를 찾는 것 역시 쉬움.(정말 적게 시간이 들어감.)
# but 받는거는 한 6~7초정도 걸림.(신경쓸거 x))
# case4.
'''
투스탭 재귀함수로 푸는 것이 맞아보임.
길이가 50 이하인 케이스에 대해서 case2를 돌릴까..?
최댓값이 항상 기준이 되야하나..?..
n,lst = input.

if len(lst) == 4:
    print(lst[1]-lst[0]+lst[3]-lst[2])
    exit(0)

min, max = min(lst),max(lst)

if min == max:
    print(0)
    exit(0)


def local_max_min(lst):
    max_num = max(lst)
    min_num = min(lst)
    max_idx = lst.index(max_num)
    min_dix = lst.index(min_num)

    if max_num == min_num or max_idx < min_dix:
        return False
    else:
        return max_num-min_num

first_dif = -inf
second_dif = -inf

# 같은 케이스는 최상위에서 reject.(단일숫자만 들어가있는 경우.)
# 길이가 4인 케이스도 최상위에서.
# Thus, 판별할 것들은 길이가 5 이상인 최소 하나의 숫자가 다른 케이스들.

if min_idx < max_idx:
    min 혹은 max가 무시되어야 하는 케이스는..? min: (1),(2),(3)에 각각 숫자가 없는 케이스에서 발생. 
    worse case: 98 0 7 4 99 10 --> 7-0 + 99-4
    gen : min((1))>min(lst)

 ~(1)~ min ~(2)~ max ~(3)~
    case_a = -inf
    case_b = -inf
    case_c = -inf
    if len((1))>=2:

    if min_idx = 1,
        (2)case, (3)case 비교.
    elif max_idx = -1,
        (1)case, (2)case 비교.
    or abs(max_idx-min(idx)) == 1:
        (1)case, (3)case 비교.  # 어디든 or로 들어가는게 가능하게 쓰기.
# maybe every case checked & done(easy?XX).

elif max_idx < min_idx:
    ~(1)~ max ~(2)~ min ~(3)~
    if max_idx != 0:
        first = min((1))
        
    if min_dix != -1:
        last = max((3))
    but if (ex. max == 100000, min((1)) = 99990),but max((2)) = 99999,min((2)) = 1 & min((2))_idx < max((2))_idx..? (WMA min = 0..)



worst case... 5 4 3 2 1.(단조감소.)

~~~~
print(first_dif+second_dif)

'''



from sys import stdin


n = int(stdin.readline()) #n>=4
nums = tuple(map(int,stdin.readline().strip().split()))

if len(nums) == 4:
    print(nums[1]-nums[0]+nums[3]-nums[2])
    exit(0)

max_num = max(nums)
min_num = min(nums)

if max_num == min_num: #모든 수가 같다는 뜻.
    print(0)
    exit(0)

max_ind = nums.index(max_num)
min_ind = nums.index(min_num)

if max_ind < min_ind :
    first = min(nums[:max_ind])
    last = max(nums[min_ind+1:])
    # 2 ~~ 4 ~~ 1 ~~ 3 이경우 1가지..?
else:
    # ~(1)~ 1 ~(2)~ 4 ~(3)~
    #3가지 비교.
    print(2)