# https://www.acmicpc.net/problem/2805

# from sys import stdin

# def res_wood_sum(lst,leng):
#     num = 0
#     for i in lst:
#         if i>leng:
#             num += i-leng 
    
#     return num

# N,M = map(int,stdin.readline().strip().split())
# woods = tuple(map(int,stdin.readline().strip().split()))
# size = max(woods)
# unit = size//2
# result = 0
# tmp = sum(woods)

# while True:
#     result = res_wood_sum(woods,size)
#     print(size)
#     if unit == 0 or result == M:
#         print(size)
#         break
    
#     if result < M:
#         size -= unit
#     elif result > M:
#         size += unit
    
#     unit = unit//2
    
    
'''
cnt_ex
2 10000
10001 20000 --> WANTED 10000, result = 10005.... unit을 빼는 과정에서 결손이 생겨서 발생하는 문제.
'''

from sys import stdin

def res_wood_sum(lst,leng):
    num = 0
    for i in lst:
        if i>leng:
            num += i-leng 
    
    return num

N,M = map(int,stdin.readline().strip().split())
woods = tuple(map(int,stdin.readline().strip().split()))

small = 0
large = max(woods)
result = 0
while True:
    mid = (small+large)//2
    result = res_wood_sum(woods,mid)
    # print(mid,result,cnt)
    if small == mid or result == M:
        print(mid)
        break
    
    if result > M:
        small = mid
    elif result < M:
        large = mid
    