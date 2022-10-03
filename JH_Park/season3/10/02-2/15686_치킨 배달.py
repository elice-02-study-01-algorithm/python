import sys
input = sys.stdin.readline
from itertools import combinations

# 치킨집의 개수는 최대 m개
n, m = map(int, input().split())

result = float("inf")
home_pos = []
chicken_pos = []
city = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(city)):
  for j in range(len(city[i])):
    if city[i][j] == 1:
        home_pos.append([i, j])
    elif city[i][j] == 2:
        chicken_pos.append([i, j])

for chick in combinations(chicken_pos, m):
    city_dis = 0
    for h in home_pos:
        each_house_dis = float("inf")
        for i in range(m):
            each_house_dis = min(each_house_dis, abs(h[0] - chick[i][0]) + abs(h[1] - chick[i][1]))
        city_dis += each_house_dis
    result = min(result, city_dis)
print(result)