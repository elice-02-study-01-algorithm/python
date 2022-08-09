from sys import stdin
input = stdin.readline

# 테스트 케이스의 개수 입력 받기
t = int(input())
# 배열 선언 (모든 case는 1만을 사용해서 만드는 방법 1가지씩은 가진다.)
dp = [1] * 10001

# 조합에 2가 추가되는 경우
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 조합에 3이 추가되는 경우
for i in range(3, 10001):
    dp[i] += dp[i - 3]

# 출력
for _ in range(t):
    print(dp[int(input())])