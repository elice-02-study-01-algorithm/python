# 미완성 코드

# 서울에서 시작해서 순서대로 한 번씩 방문하고 경산에서 끝
# 도시를 이동할 때마다 구간
# 구간 사이는 도보 혹은 자전거 이용
# 제한시간 내에 모금할 수 있는 최대 금액은?

from sys import stdin
input = stdin.readline

sections, timeLimit = map(int, input().split())
# 순서대로 (도보이동시간, 도보모금액, 자전거이동시간, 자전거모금액)
info = [tuple(map(int, input().split())) for _ in range(sections)]
print(info)
# 도보모금액과 자전거모금액 중 최대값 순서대로 정렬
info = sorted(info, key = lambda x : max(x[1], x[3]), reverse = True)
print(info)

# 다이나믹 프로그래밍인데 시간 제한, 효율?을 고려해야 함
dp = [0] * sections
dp[0] = max(info[0][1], info[0][3])
time = 0
for i in range(1, sections):
    foot, footMoney, bicycle, bicycleMoney = info[i]
    if footMoney > bicycleMoney:
        print(i)
        dp[i] += dp[i-1] + footMoney
        time += foot
    else:
        print(i)
        dp[i] += dp[i-1] + bicycleMoney
        time += bicycle

print(dp)
print(time)