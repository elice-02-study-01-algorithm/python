import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
    
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < weights[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i-1])

print(dp[N][K])