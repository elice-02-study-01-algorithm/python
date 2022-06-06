# 실험성 코드 페이지입니다. 백준이나 프로그래머스, 앨리스 문제 풀이 파일이 아녜요! - HJ -
#한글문서는 오픈 안됨.

import functools, itertools, random, math, time, sys, re, collections
import numpy as np #pandas, matplotlib 안깔림 

# 17366.

# 1654.
# from sys import stdin

# K,N = map(int,input().strip().split())
# lines = []
# for _ in range(K):
#     lines.append(int(stdin.readline().strip()))
    
# print(lines)

# maxi = 1

# dlines = [i//maxi for i in lines]
# sum(dlines) >= K
# max(maxi) = ?


# from sys import stdin
# from itertools import compress

# N,M = map(int,stdin.readline().strip().split())

# lst = list(map(int,stdin.readline().strip().split()))
# lst = list(compress(lst,map(lambda x: x<M,lst)))

# result = -1

# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             if lst[i] + lst[j] + lst[k] <= M:
#                 result = max(result,lst[i] + lst[j] + lst[k])
                
#                 if result == M:
#                     print(M)
#                     exit(0)

# print(result)

# def subsequence(arr):
#     n = len(arr) # 원소의 개수
#     result_list = [] # 생성된 부분 수열 저장
#     for i in range(1 << n): # 부분 수열 개수
#         subset = [] # 부분수열 담기 위함
#         for j in range(n): # 원소의 수만큼 비트를 비교함
#             if i & (1 << j):
#                 subset.append(arr[j]) # 부분 수열 만들기
#         result_list.append(subset)
#     return result_list

# sample_list = [ord('a'),ord('n'),ord('t'),ord('i'),ord('c')]
# print(sample_list)
# print('=====================')
# subsequence_list = subsequence(sample_list)
# print(subsequence_list) 
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


'''
4 4
79
72
70
7
WANTED: 7977270
'''
# x = [13/1,69/5,41/3,37/3,80/6]
# --> div 1 5 3 3 6
# print(x)
# print(max(x),min(x))
# print(4+2+2+5)

# x = [7,11,13]
# # --> div 3 5 5..

# mini = min(x)
# n = 1
# # x = sorted(x)
# result = math.inf
# while True:
#     temp = mini/n
#     temp_lst = []
#     for i in range(len(x)):
#         temp_lst.append(round(x[i]/temp))
#     print(temp_lst,sum(temp_lst))
    
#     temp_lst2 = [x[i]/temp_lst[i] for i in range(len(x))]
#     print(temp_lst2)
#     result = min(result,max(temp_lst2)-min(temp_lst2))
#     n+=1
#     if sum(temp_lst) > 10+3:
#         break

# print(result)

x = input()
y = input()
print(x.count(y))