## 백준 2011번
## 암호코드
## 다이나믹 프로그래밍

'''점화식
dp[n] = dp[n] + dp[n-1] -> 한자리 숫자
dp[n] = dp[n] + dp[n-2] -> 두자리 숫자
'''


def count(N):
    l = len(N)

    # dp[i] : i번째 수 단계에서 암호 코드의 개수
    dp = [0] * (l+1)

    if N[0] == 0:  # 암호 만들 수 없는 경우
        ##* print(0)
        return dp , l

    else:
        N = [0] + N  # 인덱싱을 위해 추가한 0
        dp[0] = 1
        dp[1] = 1  # 첫번째 수로 이뤄진 암호코드는 1개이다.

        for i in range(2, l+1):
            cur = N[i]  # 한 자리
            cur2 = N[i-1] * 10 + N[i]  # 두 자리
            if cur >= 1 and cur <= 9:
                dp[i] += dp[i-1]
            if cur2 >= 10 and cur2 <= 26:
                dp[i] += dp[i-2]
            dp[i] %= 1000000
        ##* print(dp[l])
        return dp, l


'''print(dp)
[1, 1, 2, 2, 4, 6]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''
if __name__ == '__main__':
    N = list(map(int, list(input())))
    counting, l = count(N)
    print(counting[l])
    ##* count(N)
