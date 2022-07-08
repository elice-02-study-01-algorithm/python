

from sys import stdin

N,K = map(int,stdin.readline().strip().split())

x,y,z,w = map(int,stdin.readline().strip().split())
dic = {x:y,z:w}
if x == z:
    dic[x] = max(y,w)

for i in range(N-1):
    lst = []
    x,y,z,w = map(int,stdin.readline().strip().split())
    if x<=z and y>=w:
        lst = [(x,y)]
    elif x>=z and y<=w:
        lst = [(z,w)]
    else:
        lst = [(x,y),(z,w)]
    temp = {}
    for j in dic:
        for k in lst:
            a,b = j + k[0], dic[j] + k[1]
            if a <= K: 
                if a not in temp:
                    temp[a] = b
                else:
                    temp[a] = max(temp[a],b)
    
    dic = temp
    
print(max(dic.values()))

# ! fourth.. 44%.. pypy도 같은 %.

# from sys import stdin

# N,K = map(int,stdin.readline().strip().split())

# x,y,z,w = map(int,stdin.readline().strip().split())
# dic = {x:y,z:w}
# for i in range(N-1):
#     x,y,z,w = map(int,stdin.readline().strip().split())
    
#     temp = {}
#     for j in dic:
#         a,b,c,d = j + x, dic[j] + y, j + z, dic[j] + w
#         if a <= K: 
#             if a not in temp:
#                 temp[a] = b
#             temp[a] = max(temp[a],b)
            
#         if c <= K:
#             if c not in temp:
#                 temp[c] = d
#             temp[c] = max(temp[c],d)
        
#     dic = temp
    
# result = 0
# for i in iter(dic.values()):
#     result = max(result,i)
    
# print(result)


# ! inital code

# from sys import stdin

# N,K = map(int,stdin.readline().strip().split())

# # 도보:시간 & 돈 + 잔차:시간 & 돈
# dic = {0:[],1:[]}
# for i in range(N):
#     x,y,z,w = map(int,stdin.readline().strip().split())
#     dic[0].append((x,y))
#     dic[1].append((z,w))

# #idx?
# lst = [dic[0][0],dic[1][0]]
# # print(dic,lst)
# for i in range(1,N):
#     temp = []
#     for k in range(len(lst)):
#         x = (dic[0][i][0] + lst[k][0],dic[0][i][1] + lst[k][1])
#         y = (dic[1][i][0] + lst[k][0],dic[1][i][1] + lst[k][1])
#         if x[0] <= K:
#             temp.append(x)
#         if y[0] <= K:
#             temp.append(y)
#     # print(temp)
#     lst = temp
# # print(lst)
# result = 0
# for i in range(len(lst)):
#     result = max(result,lst[i][1])
    
# print(result)
