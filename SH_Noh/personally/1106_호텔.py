# "적어도" goal만큼의 고객을 늘리기 위한 투자 비용의 최솟값
from sys import stdin
input = stdin.readline

def main():
    goal, cities = map(int, input().split())
    costDict = {}
    for _ in range(cities):
        cost, customer = map(int, input().split())
        costDict[customer] = cost

    customerList = costDict.keys()
    maxSize = goal + max(costDict.values())
    dp = [0] * maxSize

    for j in range(1, maxSize): # 1 ~ 10명
        minCost = float("inf")
        for k in customerList: # 3, 2, 1명
            minCost = min(minCost, dp[j-k] + costDict[k])
        dp[j] = minCost

    print(min(dp[goal:]))

if __name__ == "__main__":
    main()