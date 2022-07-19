'''
잘못된 문자열의 케이스.
n = '', '0 ~~~'
'k0' in n where k>2

n의 길이가 n[1:]을 상속받는 경우..
1. 3~9 + n[:1]

n의 길이가 n[2:]을 상속받는 경우..
--> 10 or 20 +n[2:]

n의 길이가 n[1:]+n[2:]와 같은 경우.
n[1]이 0이 아닐 때 
'''

n = list(map(int,input()))

lst = [1,1]+[0 for _ in range(len(n)-1)]

if n[0] == 0:
    print(0)
else:
    n = [0]+n
    for i in range(2,len(n)):
        if n[i]>0:
            lst[i] += lst[i-1]
        
        twonum = n[i-1]*10 + n[i]
        if twonum<=26 and twonum>=10:
            lst[i] += lst[i-2]

    print(lst[-1]%1000000)

# n = list(map(int,input()))
# l = len(n)
# dp = [0 for _ in range(l+1)]
# if (n[0] == 0) :
#     print("0")
# else :
#     n = [0] + n
#     dp[0]=dp[1]=1
#     for i in range(2, l+1):
#         if n[i] > 0:
#             dp[i] += dp[i-1]
#         temp = n[i-1] * 10 + n[i]
#         if temp >= 10 and temp <= 26 :
#             dp[i] += dp[i-2]
#     print(dp)
#     print(dp[l] % 1000000)


# n = input()

# if len(n) == 0 or ((n[0] == '0') if len(n)>0 else 1) or ('00' in n):
#     print(0)
#     exit(0)
# #길이 0인 케이스, 시작이 0인 케이스, 00이 들어가있는 케이스 reject.

# lst = [1 for _ in range(len(n))]
# if len(n)>1:
#     if n[0] == '1':
#         if n[1] != '0':
#             lst[1] = 2
#     elif n[0] == '2':
#         if n[1] in ['1','2','3','4','5','6']:
#             lst[1] = 2

# for i in range(2,len(n)):
#     if n[i-2] == '0':
#         if n[i-1] == '1':
#             if lst[i] != '0':
#                 lst[i] = 2*lst[i-1]
#             else:
#                 lst[i] = lst[i-2]
        
#         elif n[i-1] == '2':
#             if lst[i] in ['1','2','3','4','5','6']:
#                 lst[i] = 2*lst[i-1]
#             elif lst[i] in ['7','8','9']:
#                 lst[i] = lst[i-1]
#             else:
#                 lst[i] = lst[i-2]
        
#         else:  # n[i-1] = 3~9 case.  
#             if lst[i] != '0':
#                 lst[i] = lst[i-1]
#             else:
#                 print(0)
#                 exit(0) # -050- 같은 것이 있는 케이스.
            
#     elif n[i-2] == '1' or n[i-2] == '2':
#         if n[i-1] == '0':  # 1111101 1235855 
#             lst[i] = lst[i-1] # n[i] != 0이고, 뭔 수를 넣어도 갯수에 변함이 없기 때문.
#         elif n[i-1] == '1':
#             if n[i] == '0':
#                 lst[i] = lst[i-2]
#             else:
#                 lst[i] = lst[i-1]+lst[i-2]
#         elif n[i-1] == '2':
#             if n[i] == '0':
#                 lst[i] = lst[i-2]
#             elif lst[i] in ['1','2','3','4','5','6']:
#                 lst[i] = lst[i-1]+lst[-2]
#             else:
#                 lst[i] = lst[i-1]
#         else:
#             if n[i-1] == '0':
#                 print(0)
#                 exit(0)
#             else:
#                 lst[i] = lst[i-1]

#     else: #n[i-2] = 3~9, n[i-1] == 0 case는 앞에서 사라짐.
#         if n[i-1] == '1':
#             if n[i] != '0':
#                 lst[i] = 2*lst[i-1]
#             else:
#                 lst[i] = lst[i-2]
#         elif n[i-1] == '2':
#             if n[i] in ['1','2','3','4','5','6']:
#                 lst[i] = 2*lst[i-1]
#             elif n[i] == '0':
#                 lst[i] = lst[i-2]
#             else:
#                 lst[i] = lst[i-1]
        
#         else:
#             if n[i] == '0':
#                 print(0)
#                 exit(0)
#             else:
#                 lst[i] = lst[i-1]
            
# print(lst)
# 111013 --> 2.. 1 2 3 2 2 4
# 1010 --> 1.. 1 1 1 1
# 1110 --> 2.. 1 2 3 2  
    
    # if n[i-2] == '1':
    #     if n[i-1] != '0':
    #         if n[i] != '0':
    #             lst[i] = lst[i-1] + lst[i-2]
    #         else:
    #             lst[i] = lst[i-2]
    #     else:
    #         lst[i] = lst[i-2]
    # elif n[i-2] == '2':
    #     if n[i-1] in ['1','2','3','4','5','6']:
    #         lst[i] = lst[i-1] + lst[i-2]
    #     elif n[i-1] == '0':
    #         lst[i] = lst[i-3]
    #     else:
    #         lst[i] = lst[i-1]
    # elif n[i-2] == '0':
    #     if n[i-3] == '1' or n[i-3] == '2':
    #         lst[i] = lst[i-3]
    #     else:
    #         lst[i] = 0
    # else:
    #     lst[i] = lst[i-1]

# print(lst)
# print(lst[-1]%1000000)
# 14%... 똑같은 곳에서 틀림.... 2의 문제가 아니라 다른 문제가 있는 것인데... 뭐일까..?...


# 1111111111 --> 89
# 11111111110 --> 55
# 25114 --> 6
# 12 
# n 바로 뒤에 1 혹은 2가 붙는 경우.
# 점화식으로 하는 것은 상당히 난해... 12340169 이런 것이 있을 가능성이 있고,
# 0169 바로 앞에 1혹은 2가 들어갈 가능성이 있기 때문.
# 0 1 1 2 3 5 8 13 21 34 55..?
# 0 1 2 3 4 5 6 7  8  9  10
# 11 11 11 11 11
# 1 1 1 1 1 1 1 1 1
# 1 2 3 5 8 13 21 34 55 89..?
