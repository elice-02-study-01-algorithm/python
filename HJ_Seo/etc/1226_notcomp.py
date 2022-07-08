from sys import stdin
n = int(input())
dang = [0] + list(map(int,stdin.readline().strip().split()))

total = sum(dang)


#  Link : https://www.acmicpc.net/problem/1226
# ! inital code.. 작은 N case에 대해서는 쉽게 done.. 30개 넘어가면 x.
# from sys import stdin
# from itertools import combinations

# n = int(input())
# dang = [0] + list(map(int,stdin.readline().strip().split()))

# total = sum(dang)

# complete = []
# for i in range(1,n):
#     for j in combinations(dang[1:],i):
#         if sum(j)>=total/2:
#             if sum(j)-min(j)<total/2:
#                 complete.append(j)

# first = complete[0]

# for i in complete:
#     if sum(first)<sum(i):
#         first = i

# idx = []
# for i in range(n+1):
#     if dang[i] in first:
#         idx.append(i)

# print(len(idx))
# print(*idx)