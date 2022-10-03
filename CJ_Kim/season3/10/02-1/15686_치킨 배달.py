import sys
from itertools import combinations
input = sys.stdin.readline

citySize, limitCH = map(int, input().split())

chickenDistanceInfo = {}
chickenInfo = []
houseInfo = []

# 치킨집이랑 일반집 담아주기
for i in range(1, citySize+1):
    rowInfo = list(map(int, input().split()))
    for colIndex in range(1, citySize+1):
        if rowInfo[colIndex-1] == 1:
            houseInfo.append((i, colIndex))
        elif rowInfo[colIndex-1] == 2:
            chickenInfo.append((i, colIndex))

# 치킨거리 표 만들기 예시는 아래 주석에!
for chickenZip in chickenInfo:
    cR, cC = chickenZip
    chickenDistanceInfo[chickenZip] = []
    for house in houseInfo:
        hR, hC = house
        chickenDistance = abs(cR-hR) + abs(cC-hC)
        chickenDistanceInfo[chickenZip].append(chickenDistance)

# print(chickenDistanceInfo)
# 행은 치킨집, 열은 일반집
# {      (1, 3)(2, 5)(3, 2)(4, 3)
# (2, 3): [1,    2,    2,    2], 
# (3, 3): [2,    3,    1,    1], 
# (5, 5): [6,    3,    5,    3]}

# chickenDistanceInfo dictionary 형태로 들어가면 치킨 거리 구해주는 함수
def calculateChickenDistance(info):
    totalDistance = 0
    for i in range([len(value) for key, value in info.items()][0]):
        minDistanceEachHouse = float('inf')
        for key, value in info.items():
            if value[i] < minDistanceEachHouse:
                minDistanceEachHouse = value[i]
        totalDistance += minDistanceEachHouse
    return totalDistance

# 만약 있어야 하는 치킨집 개수가 현재 치킨집 개수와 같으면 바로 치킨 거리 구하기
if len(chickenDistanceInfo) == limitCH:
    print(calculateChickenDistance(chickenDistanceInfo))
# 현재 치킨집 개수가 더 많으면 조합으로 최소 거리를 가지는 경우 구하기
else:
    minChickenDistance = float('inf')
    # 치킨집이 5개이고, 있어야하는 수가 2면 5Comnibation2
    for selectedChickenHouses in combinations(chickenInfo, limitCH):
        selectedChickenInfo = {}
        # 뽑힌 치킨집들 가지고 info 만들기
        for chickenHouse in selectedChickenHouses:
            selectedChickenInfo[chickenHouse] = chickenDistanceInfo[chickenHouse]
        # 만든 info로 치킨 거리 구하기
        tempMinValue = calculateChickenDistance(selectedChickenInfo)
        # 최솟값 갱신해주기
        if tempMinValue < minChickenDistance:
            minChickenDistance = tempMinValue
    print(minChickenDistance)
