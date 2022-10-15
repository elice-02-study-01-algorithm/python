'''
방법1 : 시간초과
pypy로는 시간초과 안남.
'''

# 중복조합 : from itertools import combinationswith_replacement

# def fibo(x):
#     # 종료 조건
#     if x == 1:
#         return i
#     if x == 2:
#         return j
#     # 이미 계산한 적 있는 문제라면 그대로 반환
#     if dp[x] != 0:
#         return dp[x]
#     # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#     dp[x] = fibo(x-1) + fibo(x-2)
#     return dp[x]

# d, k = map(int,input().split())

# cur = False
# for i in range(1,50001):
#     for j in range(i,100001):
#         dp = [0] * 31
#         if k == fibo(d):
#             # result.append(i)
#             # result.append(j)
#             print(i)
#             print(j)
#             cur = True
#             break
#     # if result:
#     #     break
#     if cur:
#         break
# # print(*result, sep='\n')

'''
방법2 : 성공
fibo(1), fibo(2)
fibo(3) = fibo(2) + fibo(1)
fibo(4) = fibo(3) + fibo(2) = 2 * fibo(2) + fibo(1)
fibo(5) = fibo(4) + fibo(3) = 3 * fibo(2) + 2 * fibo(1)
fibo(6) = fibo(5) + fibo(4) = 5 * fibo(2) + 3 * fibo(1)
'''

d, k = map(int,input().split())

dp = [(0,0)] * 31
dp[1] = (1,0)
dp[2] = (0,1)
for i in range(3, d+1):
    dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])


for i in range(1,50001):
    for j in range(i,100001):
        if k == (i*dp[d][0] + j*dp[d][1]):
            print(i)
            print(j)
            exit()