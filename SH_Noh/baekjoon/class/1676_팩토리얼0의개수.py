# 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 영의 개수 구하기
# (2 * 5) 세트의 횟수를 구하면 됨
# N은 최대 500

from sys import stdin

N = int(stdin.readline())
dp = [0 for _ in range(N+1)]

for i in range(2, N+1):
    # 2는 진짜 엄청 많음, 5가 있어야 함
    five = 0
    cur = i
    while cur % 5 == 0:
        five += 1
        cur //= 5
    dp[i] = dp[i-1] + five

print(dp[-1])