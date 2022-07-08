# n가지 종류의 동전의 합이 k원이 되도록
# 동전의 개수는 무제한
from sys import stdin

kind, total = map(int, stdin.readline().split())
kindList = []
for _ in range(kind):
    kindList.append(int(stdin.readline()))
# print(kindList)

dp = [0] * (total + 1)
dp[0] = 1
for i in kindList: # 1, 2, 5원짜리 동전
    for j in range(i, total + 1):
        if dp[j-i] != 0: 
            dp[j] += dp[j-i]
print(dp[-1])
# print(dp)