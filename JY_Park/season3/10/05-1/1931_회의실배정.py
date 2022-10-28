# import sys
# input = sys.stdin.readline
# n = int(input())
# time = []
# for i in range(n):
#     start, end = map(int,input().split())
#     time.append((start, end))
# time_sort = sorted(time, key=lambda x:(x[1],x[0]))
# # print(time_sort)

# end_time = time_sort[0][1]
# count = 1
# for i in range(1, n):
#   if end_time <= time_sort[i][0]:
#     count+=1
#     end_time = time_sort[i][1]
# print(count)

'''
[복습] 22.10.25
'''

# 시도1
# import sys
# input = sys.stdin.readline

# n = int(input())
# time_table = []
# for i in range(n):
#   start, end = map(int,input().split())
#   time_table.append((start, end))

# time_table.sort()
# max_num = 0
# for i in range(n):
#   temp = time_table[i][1]
#   count = 1
#   for j in range(i,n):
#     if time_table[j][0] >= temp:
#       count += 1
#       temp = time_table[j][1]
  
#   if count >= max_num:
#     max_num = count

# print(max_num)


import sys
input = sys.stdin.readline

n = int(input())
time_table = []
for i in range(n):
  start, end = map(int,input().split())
  time_table.append((start, end))

# 정렬 기준 : 시작 시간, 회의 시간이 짧은거
# 다시 생각 : 빨리 끝날수록 최대 회의를 사용할 가능성 높아짐.

# time_table.sort()
# time_table.sort(key = lambda x :(x[0], x[1]-x[0]))
time_table.sort(key = lambda x :(x[1], x[0]))
print(time_table)

temp = time_table[0][1]
count = 1
for i in range(1,n):
  if time_table[i][0] >= temp:
    count += 1
    temp = time_table[i][1]
  
print(count)

# 5%에서 시간 초과
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# time_table = []
# for i in range(n):
#   start, end = map(int,input().split())
#   heapq.heappush(time_table,(start, end))

# max_num = 0
# for i in range(n):
#   temp = time_table[i][1]
#   count = 1
#   for j in range(i,n):
#     if time_table[j][0] >= temp:
#       count += 1
#       temp = time_table[j][1]
  
#   if count >= max_num:
#     max_num = count
# print(time_table)
# print(max_num)