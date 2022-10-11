from sys import stdin
input = stdin.readline

glass = int(input())
wine = [int(input()) for _ in range(glass)]
dp = [0] * glass

if glass < 3:
    print(sum(wine))
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
    for i in range(3, glass):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    # print(dp)
    print(dp[-1])
