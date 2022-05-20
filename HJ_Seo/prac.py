# 실험성 코드 페이지입니다. 백준이나 프로그래머스, 앨리스 문제 풀이 파일이 아녜요! - HJ -
#한글문서는 오픈 안됨.

import functools, itertools, random, math, time
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

