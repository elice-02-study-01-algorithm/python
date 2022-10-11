import sys
input = sys.stdin.readline
 
n = int(input())
wine_list = [0]
for _ in range(n):
    wine_list.append(int(input()))

dp = [0, wine_list[1]]
if n > 1:
    dp.append(wine_list[1] + wine_list[2])

for i in range(3, n+1):
    # i-1 번째 잔을 먹지 않아! -> i-2 번째 까지의 최대값 (dp)와 지금 주스 마시면 됨
    one = dp[i-2] + wine_list[i]
    # i-2 번째 잔을 먹지 않아! -> i-3번째 까지의 최대값 (dp)와 이전 주스랑 이번 주스 마시면 됨
    two = dp[i-3] + wine_list[i-1] + wine_list[i]
    # i-1도, i-2도 마셔버렸어! -> 이번꺼 패스
    three = dp[i-1]
    dp.append(max(one, two, three))
print(dp[n])