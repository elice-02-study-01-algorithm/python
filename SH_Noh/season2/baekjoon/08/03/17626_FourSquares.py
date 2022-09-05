from sys import stdin
input = stdin.readline

n = int(input())
# dp[i] = 숫자 i가 가지는 제곱수 합 최소개수
dp = [float("inf")] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    for j in range(1, i + 1):
        double = j * j
        if double > i:
            break
        if dp[i] > dp[i-double] + 1:
            dp[i] = dp[i-double] + 1
print(dp[n])