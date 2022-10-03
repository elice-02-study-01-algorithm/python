from sys import stdin
input = stdin.readline

# def maximum(N, profits, dp):
#     sum = 0
#     for i in range(1, N + 1):
#         sum += profits[i]
#         dp[i] = dp[i-1] if dp[i-1] > sum else sum

if __name__ == "__main__":
    while True:
        N = int(input())
        if N == 0:
            break
        profits = [int(input()) for _ in range(N)]
        for i in range(1, N):
            if profits[i] < profits[i] + profits[i-1]:
                profits[i] = profits[i] + profits[i-1]

        print(max(profits))