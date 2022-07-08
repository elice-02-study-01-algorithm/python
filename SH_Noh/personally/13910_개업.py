# 최소 몇 번의 요리로 주문을 처리할 수 있는지
from sys import stdin
from itertools import combinations

noodle, wok = map(int, stdin.readline().split())
wokSize = list(map(int, stdin.readline().split()))

# 양손잡이가 한 번의 요리로 만들 수 있는 모든 noodle 개수 집합
wokCombi = set(wokSize)
combi = combinations(wokSize, 2)
for j in combi:
    wokCombi.add(sum(j))
# print(wokCombi)

# wokCombi에서 몇 번을 더해야 noodle 개수가 될지 동적계획법
dp = [0] * (noodle + 1)
if noodle in wokCombi:
    print(1)
else:
    for i in range(1, len(dp)):
        minVal = float("inf")
        for x in wokCombi:
            if (i-x >= 0):
                minVal = min(minVal, dp[i-x] + 1)
        dp[i] = minVal
    print(-1 if dp[-1] == float("inf") else dp[-1])
# print(dp)