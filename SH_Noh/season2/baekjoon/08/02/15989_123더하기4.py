from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        num = int(input())
        dp = [1] * (num + 1)
        for i in range(2, num + 1):
            dp[i] += dp[i-2]
        for i in range(3, num + 1):
            dp[i] += dp[i-3]
        print(dp[num])
