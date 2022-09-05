from sys import stdin

# A = 1, B = 2, C = 3... Z = 26
# 한 자리수 아니면 두 자리수
# 두 자리수의 경우 27부터는 불가능

# 한 자리 수 : convert[x] = convert[x-1] + convert[x]
# 두 자리 수 : convert[x] = convert[x-2] + convert[x]

code = list(map(int, stdin.readline().strip()))
l = len(code)
dp = [0 for _ in range(l+1)]

if code[0] == 0: # 0으로 시작하면 잘못된 코드
    print("0")
else:
    code = [0] + code # 인덱스 맞춰주기 위해
    dp[0] = dp[1] = 1
    for i in range(2, l+1):
        if code[i] > 0:
            dp[i] += dp[i-1]
        temp = code[i-1] * 10 + code[i] # 앞자리와 합쳐줌
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]
    print(dp[l] % 1000000)

# https://jyeonnyang2.tistory.com/55