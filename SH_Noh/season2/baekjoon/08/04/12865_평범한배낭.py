# N개의 물건은 W의 무게와 V의 가치를 가짐
# 최대 K개의 무게만 넣을 수 있는 가방
# 가치의 최댓값은?

from itertools import product
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
products = [tuple(map(int, input().split())) for _ in range(N)]
# dp[i][j]는 무게 i에 대해 물건 j를 담거나 담지 않는 경우 중 최댓값
dp = [[0 for _ in range(K + 1)] for _ in range(N)]
for i in range(0, N):
    for j in range(1, K + 1):
        weight = products[i][0]
        value = products[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N - 1][K])