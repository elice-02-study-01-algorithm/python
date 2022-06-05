# 한 번에 한 계단 또는 두 계단씩 오를 수 있음
# 연속된 세 개의 계단을 모두 밟아서는 안 됨
# 마지막 도착 계단은 반드시 밟아야 함
# 얻을 수 있는 총 점수의 최댓값은?

from sys import stdin
input = stdin.readline

stairs = int(input())
scores = [int(input()) for _ in range(stairs)]

dp = [0] * stairs
if stairs < 3:
    print(sum(scores))
else:
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, stairs):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i] + scores[i-1])

    print(dp[-1])
