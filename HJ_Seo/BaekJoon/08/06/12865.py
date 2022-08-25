# https://www.acmicpc.net/problem/12865

# from sys import stdin
# N,total = map(int,stdin.readline().strip().split())

# items = []

# for i in range(N):
#     weight,value = map(int,stdin.readline().strip().split())
#     if weight>total:
#         value = 0
#     items.append((weight,(1<<i),value))

# init = set(items)

# results = set()
# while True:
#     next = set()
#     for i in init:
#         tmp = 0
#         for j in items:
#             if i[0]+j[0]<=total and i[1]&j[1] == 0:
#                 next.add((i[0]+j[0],i[1]+j[1]))
#                 tmp = 1
        
#         if tmp == 0:
#             results.add(i[1])

#     if len(next) == 0:
#         result = 0
#         for i in results:
#             tmp = 0
#             for j in range(N):
#                 if i & (1<<j):
#                     tmp += items[j][2]
#             result = max(result,tmp)
        
#         print(result)
#         break
    
#     init = next

# ! 시간초과..?..

# from sys import stdin
# N,total = map(int,stdin.readline().strip().split())

# items = []
# for i in range(N):
#     weight,value = map(int,stdin.readline().strip().split())
#     if weight>total:
#         continue
    
#     items.append((weight,value))

# N = len(items)
# items = sorted(items)

# not_use_idx = [set(i for i in range(N)) for _ in range(total+1)]
# maxi_value_per_weight = [0]*(total+1)

# for i in range(N):
#     weight,value = items[i]
#     if maxi_value_per_weight[weight]<value:
#         maxi_value_per_weight[weight] = value
#         not_use_idx[weight] = set(i for i in range(N)) - {i}

# # print(maxi_value_per_weight)

# for i in range(1,total):
#     if maxi_value_per_weight[i]<maxi_value_per_weight[i-1]:
#         maxi_value_per_weight[i]=maxi_value_per_weight[i-1]
#         not_use_idx[i] = not_use_idx[i-1]
#     for j in not_use_idx[i]:
#         if i+items[j][0]<=total:
#             tmp_weight = i+items[j][0]
#             if maxi_value_per_weight[tmp_weight]<maxi_value_per_weight[i]+items[j][1]:  # ! 값이 같아지는 경우에 대한 고려가 필요..
#                 maxi_value_per_weight[tmp_weight] = maxi_value_per_weight[i]+items[j][1]
#                 not_use_idx[tmp_weight] = not_use_idx[i]-{j}
                
#     # print(maxi_value_per_weight[i])
#     # print(not_use_idx[i])

# print(maxi_value_per_weight[-1])
# # print(maxi_value_per_weight)

# ! !!!!!!!!!!!!!!!!!!!!

# from sys import stdin
# N,total = map(int,stdin.readline().strip().split())

# items = []
# for i in range(N):
#     weight,value = map(int,stdin.readline().strip().split())
#     if weight>total:
#         continue
    
#     items.append((weight,value))

# result = 0

# for i in range(1,(1<<N)):  # ! 단순히 여기때문에 느려지는거.. 2**100을 언제다까..
#     get_weight = 0
#     get_value = 0
#     for j in range(N):
#         if i & (1<<j): 
#             get_weight += items[j][0]
#             get_value += items[j][1]
#     if get_weight<=total:
#         result = max(result,get_value)

# print(result)

# ! 무식한 코드... 풀체크하는게 아님..

# from sys import stdin
# from collections import deque
# N,total = map(int,stdin.readline().strip().split())

# weights = []
# values = []
# for i in range(N):
#     weight,value = map(int,stdin.readline().strip().split())
#     if weight>total:
#         continue
    
#     weights.append(weight)
#     values.append(value)

# N = len(weights)

# if N == 0:
#     print(0)
#     exit(0)

# TF_idx = [False]*N

# result = 0
# Q = deque()
# for i in range(N):
#     tmp = TF_idx.copy()
#     tmp[i] = True
#     Q.append([weights[i],tmp])
# # print(Q)

# while True:
#     info = Q.popleft()
#     # print(info)
#     for idx in range(N):
#         if info[0]+weights[idx]<=total and info[1][idx] == False:
#             comb = [info[0]+weights[idx],info[1].copy()]
#             comb[1][idx] = True
#             if comb not in Q:
#                 Q.append(comb)
#     else:
#         tmp = 0
#         for i in range(N):
#             tmp += values[i] if info[1][i] == True else 0
#         result = max(result,tmp)
        
#     if len(Q) == 0:
#         print(result)
#         break

# ! 역시 시간초과.

# ! https://hongcoding.tistory.com/50 .. 냅섹 알고리즘..?..

from sys import stdin
N,total = map(int,stdin.readline().strip().split())

weights = [0]
values = [0]
for i in range(N):
    weight,value = map(int,stdin.readline().strip().split())
    if weight>total:
        continue
    
    weights.append(weight)
    values.append(value)

N = len(weights)
goods_weight_per_value = [[0]*(total+1) for _ in range(N)]

for i in range(1, N):
    for j in range(1, total+1):
        w = weights[i]
        v = values[i]
        
        if j<w:
            goods_weight_per_value[i][j] = goods_weight_per_value[i-1][j]
        else:
            goods_weight_per_value[i][j] = max(goods_weight_per_value[i-1][j], goods_weight_per_value[i-1][j-w]+v)

print(goods_weight_per_value[-1][-1])
# for i in goods_weight_per_value:
#     print(i)

# ! 아래 코드는 효율적인 코드.

import sys
input = sys.stdin.readline

def get_max_value_case(K):
    dp = [0] * (K + 1)
    for w, v in WV:
        for i in range(K, -1, -1):
            if i - w < 0:
                break
            dp[i] = max(v + dp[i - w], dp[i])
    return dp[K]

n, k = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(n)]
WV.sort()

print(get_max_value_case(k))

'''
bad case : 
100 6000
1 3
2 5
3 7
4 9
5 11
6 13
7 15
8 17
9 19
10 21
11 23
12 25
13 27
14 29
15 31
16 33
17 35
18 37
19 39
20 41
21 43
22 45
23 47
24 49
25 51
26 53
27 55
28 57
29 59
30 61
31 63
32 65
33 67
34 69
35 71
36 73
37 75
38 77
39 79
40 81
41 83
42 85
43 87
44 89
45 91
46 93
47 95
48 97
49 99
50 101
51 103
52 105
53 107
54 109
55 111
56 113
57 115
58 117
59 119
60 121
61 123
62 125
63 127
64 129
65 131
66 133
67 135
68 137
69 139
70 141
71 143
72 145
73 147
74 149
75 151
76 153
77 155
78 157
79 159
80 161
81 163
82 165
83 167
84 169
85 171
86 173
87 175
88 177
89 179
90 181
91 183
92 185
93 187
94 189
95 191
96 193
97 195
98 197
99 199
100 201
'''