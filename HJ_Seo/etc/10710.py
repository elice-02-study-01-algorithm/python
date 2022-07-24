# from sys import stdin

# N,M = map(int,stdin.readline().strip().split())

# D_i = [int(stdin.readline().strip()) for _ in range(N)]
# C_i = [int(stdin.readline().strip()) for _ in range(M)]
# x = max(C_i)*M*max(D_i)*N+1
# need = [[0]*(M+1)]+[[x]*(M+1) for _ in range(N)]

# for i in range(1,N+1): # i번째 도시.
#     for j in range(i,M+1): #j번째 날에 방문., i날에 방문가능한 최소 도시 번호 = i
#         need[i][j] = min(need[i][j],min(need[i-1][i-1:j])+C_i[j-1]*D_i[i-1])
        
# print(min(need[-1]))

# ! 이거 왜 시간초과니??
# for i in need:
#     print(i)

from sys import stdin

N,M = map(int,stdin.readline().strip().split())

D_i = [int(stdin.readline().strip()) for _ in range(N)]
C_i = [int(stdin.readline().strip()) for _ in range(M)]
x = max(C_i)*M*max(D_i)*N+1
temp = [0 for _ in range(M+1)] #기준 도시
temp2 = [x for _ in range(M+1)] #init.
temp3 = temp2.copy() # 다음 도시.

for i in range(1,N+1): # i번째 도시.
    # print(temp) # ! check1
    for j in range(i,M+1): #j번째 날에 방문., i날에 방문가능한 최소 도시 번호 = i
        # print(i,j)
        temp3[j] = min(temp3[j],min(temp[i-1:j])+C_i[j-1]*D_i[i-1])
    temp = temp3
    temp3 = temp2.copy()
# print(temp) # ! check2
print(min(temp))

# ! 이건 맞는데.... 시간이 너무 괴랄...,,ㅠ