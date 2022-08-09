# 실버1

# 보텀업 -> 너무 오래걸림.
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    d = [0] * 10001
    d[1] = 1
    d[2] = 2
    d[3] = 3

    for i in range(4, n+1):
        # d[i] = d[i-1] + d[i-2] + d[i-3]
        d[i] = d[i-1] + (d[i-2] - d[i-3])
        if i % 3 == 0:
            d[i] += 1
    print(d[n])


# 탑다운
# t = int(input())

# # 경우의 수를 저장할 리스트 초기화 (1의 합으로 나타내는 방법은 1가지씩 존재)
# '''
# 1 : 1 (1가지)
# 2 : 1+1, 2 (2가지)
# 3 : 1+1+1, 2+1, 3 (3가지)
# 4 : 1+1+1+1, 2+1+1, 3+1, 2+2 (4가지)
# 5 : 1+1+1+1+1, 2+1+1+1, 3+1+1, 2+2+1, 3+2, 5 (5가지)
# 6 : 1+1+1+1+1+1, 2+1+1+1+1, 3+1+1+1, 2+2+1+1,3+2+1, 2+2+2, 3+3, 6 (7가지)
# 7 : (8가지)
# '''
# d = [1] * 10001

# def combination(n):
#     for i in range(2, 10001):
#         dp[i] 
        
#     for i in range(3, 10001):


# for _ in range(t):
#     n = int(input())
#     combination(n)