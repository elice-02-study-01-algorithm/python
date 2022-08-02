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

# from sys import stdin
# N,M = map(int,stdin.readline().strip().split())
# trees = tuple(map(int,stdin.readline().strip().split()))

# if sum(trees) == M:
#     print(0)
#     exit(0)

# cut_res = []
# x = max(trees)
    
# temp = x//2
# while temp != 0:
#     cut_res = [0 for _ in range(N)]
#     for i in range(N):
#         if x<trees[i]:
#             cut_res[i] = trees[i]-x
    
#     if sum(cut_res) == M:
#         print(x)
#         exit(0)
    
#     if sum(cut_res) > M:
#         x += temp
#     else:
#         x -= temp
#         temp = x//2
    
# print(x)

# from sys import stdin
    
# x,y = map(int,stdin.readline().strip().split())

# grape = {x:[]}
# temp = []
# for i in range(y-1):
#     a,b = map(int,stdin.readline().strip().split())
#     if a in grape:
#         grape[a].append(b)
#         grape[b] = []
#     elif b in grape:
#         grape[b].append(a)
#         grape[a] = []
#     else:
#         temp.append((a,b))

# while len(temp) != 0:
#     for i in temp:
#         if i[0] in grape:
#             grape[i[0]].append(i[1])
#             grape[i[1]] = []
#         elif i[1] in grape:
#             grape[i[1]].append(i[0])
#             grape[i[0]] = []
#         temp.remove(i)

# rearr = []
# while True:
#     if len(grape) == 0:
#         break
    
#     leaf = []
#     for i in grape:
#         if len(grape[i]) == 0:
#             leaf.append(i)

#     rearr.append(leaf)
    
#     for i in leaf:
#         del grape[i]
    
#     for i in grape:
#         grape[i] = [j for j in grape[i] if j not in leaf]

# print(len(rearr))

# for i in rearr:
#     print(*sorted(i))
    
# =========================================================================

# from sys import stdin

# def main():
#     x = int(input())
#     lst = list(map(int,stdin.readline().strip().split()))

#     sum_num = sum(lst)

#     while len(lst) != 1:
#         mini = float('inf')
#         for i in range(len(lst)-1):
#             mini = min(mini,lst[i]*lst[i+1])
        
#         for i in range(len(lst)-1):
#             if lst[i]*lst[i+1] == mini:
#                 lst = lst[:i] + [max(lst[i],lst[i+1])] + lst[i+2:]
#                 sum_num += mini
#                 break
        
#     print(sum_num)

# if __name__=="__main__":
#     main()
    
# =========================================================================

# from itertools import combinations
# from sys import stdin

# def main():
#     x = int(input())
#     dots = [tuple(map(int,stdin.readline().strip().split())) for _ in range(x)]

#     cnt = 0
#     for i in combinations(dots,3):
#         if (i[1][0]-i[0][0])*(i[2][1]-i[0][1]) != (i[2][0]-i[0][0])*(i[1][1]-i[0][1]):
#             cnt += 1
    
#     print(cnt)

# if __name__=="__main__":
#     main()

# print(len(tuple(filter(lambda x : x>=2 and x<=3,[]))))

# print(tuple({1,4,6})[2])

n = input()

checknum = 1
while True:
    n_change = ''
    for i in n[:8]:
        n_change += chr(ord(i) ^ checknum)
    
    if n_change == 'CHICKENS':
        # print(checknum)
        break
    
    checknum += 1
    
n_before = 'CHICKENS'
for i in n[8:]:
    n_before += chr(ord(i) ^ checknum)

print(n_before)

# for i in 'CHI':
#     print(bin(ord(i)))
#     print(bin(ord(i)^22))
#     print('===')
# print(bin(22))

# ! 이게 왜 정답이야???...

for x in input():print(end=chr(ord(x)^22))