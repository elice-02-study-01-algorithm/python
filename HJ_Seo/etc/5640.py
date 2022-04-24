#백준 5640번.
from sys import stdin

# == func part ==
def c(lst,i):
    if lst[i] == 0:
        lst[i] = 1
    else:
        lst[i] = 0

def compress_changer(lsts,n):
    for i in range(len(lsts)):
        lst = [0 for _ in range(n+1)]
        for j in lsts[i]:
            lst[j] = 1
        lsts[i] = lst
    
    return lsts

def func(f,comp_elts):
    
    return 

# == func part ==
case = int(input())

result = ''

while True:
    n,m = map(int,input().strip().split())

    f = [0 for _ in range(n+1)]
    f_not = [1 for _ in range(n+1)]

    Ses = [list(map(int,stdin.readline().strip().split())) for _ in range(m)]
    Ses = compress_changer(Ses,n)

    # f의 원소들을 하나하나 True로 바꿔주면서 비교할 수 있는 함수. 
    # 함수 내 len(set(itertools.compress(f,Si))) = 2 일 경우 다른거 없이 return 'T' 계속 1일 경우 return 'F'--> result += ~~ 처리.
    c(f,0)
    c(f,1) #처음.

    while True:
        if f == f_not: #비교를 했는데 함수가 없었다..
            result += "N"
            break
        








    if case != 1:
        case -=1
        empty = input() #공백인 줄간격.
    else:
        break

print(result) 

#? ==========================================================

##### partition으로 나눠볼까??..  (XX)

# from sys import stdin

# case = int(input())
# result = ''

# while True:
#     n,m = map(int,input().strip().split())

#     U = set([i for i in range(1,n+1)])

#     Ses = []
#     for _ in range(m):
#         Ses.append(set(map(int,stdin.readline().strip().split())))

#     S_full = Ses[0].copy()

#     cnt = 0
#     while True:
#         if cnt == m-1:
#             # print('compare. =',S_full,U)
#             if S_full == U:
#                 # print("Y")
#                 result += "Y"
#             else:
#                 # print("N")
#                 result += "N"
            
#             break
        
#         for i in Ses[1:]:
#             if len(S_full & i) != 0 and S_full & i != i:
#                 S_full = S_full | i
#                 # print(S_full)

#         cnt += 1

#     if case != 1:
#         case -=1
#         empty = input() #공백인 줄간격.
#     else:
#         break

# print(result) 