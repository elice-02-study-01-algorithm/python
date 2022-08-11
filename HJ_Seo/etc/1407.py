'''
5 9
--> 1 2 1 8 1 ==> sum : 13
'''

# from sys import stdin

# seq = [0]
# sum_seq = [0]

# N,M = map(int,stdin.readline().strip().split())
# target = 0
# for i in range(1,M+1):
#     if i%2 == 1:
#         target = 1
#     else:
#         target = 2 * seq[i//2]
    
#     seq.append(target)
#     sum_seq.append(target+sum_seq[-1])

# print(sum_seq[M] - sum_seq[N-1])

# ! 메모리 초과.

# from sys import stdin

# sum_seq = 0

# def div_two(num):
#     cnt = 1
#     while True:
#         if num%2 != 0:
#             return cnt
        
#         cnt *= 2
#         num = num//2

# N,M = map(int,stdin.readline().strip().split())

# for i in range(N,M+1):
#     if i%2 == 1:
#         sum_seq += 1
#     else:
#         sum_seq += div_two(i)

# print(sum_seq)

# ! 시도 X but 안봐도 시간이든 메모리든 초과.

# from sys import stdin

# N,M = map(int,stdin.readline().strip().split())

# nums = {i for i in range(N,M)}
# result = 0
# tmp = 1

# while True:
#     tmp_nums = set()
#     cnt = 0
#     while len(nums) != 0:
#         x = nums.pop()
#         if x%2 == 1: # 홀수이면
#             cnt += 1
#         else:
#             tmp_nums.add(x//2)
    
#     result += tmp*cnt
#     tmp *= 2
#     if len(tmp_nums) == 0:
#         break

#     nums = tmp_nums

# print(result)

# ! 이것도 메모리 초과.. 그냥 받으면 무조껀 메모리초과 나겠네..

# from sys import stdin

# N,M = map(int,stdin.readline().strip().split())

# result = 0
# tmp = 1
# M+=1

# while True:
#     cnt = 0
#     tmp1 = (N+1)//2
#     tmp2 = (M+1)//2
#     for i in range(N,M):
#         if i%2 == 1:
#             cnt += 1
    
#     result += tmp*cnt
#     tmp *= 2
    
#     if tmp1 == tmp2:
#         break
    
#     N,M = tmp1,tmp2
    
# print(result)

# ! 이건 시간초과. for문을 이용해서 푸는게 또 아니네.. cnt는 홀수의 갯수.

from sys import stdin

N,M = map(int,stdin.readline().strip().split())

result = 0
tmp = 1
M+=1

while True:
    cnt = M//2 - N//2
    tmp1 = (N+1)//2
    tmp2 = (M+1)//2
    
    result += tmp*cnt
    tmp *= 2
    
    if tmp1 == tmp2:
        break
    
    N,M = tmp1,tmp2
    
print(result)

'''
176 177(178) * 1
88 (89) *
44 (45) *
22 (23) *
11 (12) 16

5 6 7 8 9 (4,10) 1 * 1 * 1
  3   4   (2,5 )   2   *
      2   (1,3 )          *
      1              8

'''