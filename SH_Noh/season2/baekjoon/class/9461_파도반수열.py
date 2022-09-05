from sys import stdin
input = stdin.readline

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(0, 98):
    dp[i+3] = dp[i] + dp[i+1]

case = int(input())
for i in range(case):
    n = int(input())
    print(dp[n])