# dp[i] = dp[i -1] + dp[i -2]
import sys
input = sys.stdin.readline

d, k = map(int, input().split())

dp = [0 for i in range(d)]
dp[0], dp[1] = 1, 1

while 1:
    for i in range(2, d):
        dp[i] = dp[i-1] + dp[i -2]
    if dp[-1] == k:
        print(dp[0])
        print(dp[1])
        break
    # 첫번째 값과 두번째 값의 차이가 너무 크다
    elif dp[-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    # 첫번째 값과 두번째 값의 차이가 너무 작다
    else:
        dp[1] += 1