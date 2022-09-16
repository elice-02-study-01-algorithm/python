import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

# prefix_sum = [0]
# for i in range(n):
#     prefix_sum.append(prefix_sum[i]+int(input()))

dp = [0] * n

# 계속 최댓값만 누적될 수 있도록

dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]
    if n == 2:
        print(dp[1])
        exit(0)
    # 이때부터는 선택권이 생김
    # wine = [6, 10, 13, // 9, 8, 1]
    dp[2] = max(dp[0]+wine[2], dp[1], wine[1]+wine[2])

    for i in range(3,n):
        dp[i] = max(dp[i-2]+wine[i], dp[i-1], wine[i-1]+wine[i]+dp[i-3])

print(dp[n-1])