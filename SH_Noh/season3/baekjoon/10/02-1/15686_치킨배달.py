from itertools import combinations
from sys import stdin
input = stdin.readline

# 각 칸은 0빈 칸/1집/2치킨집 중 하나
# 치킨 거리 = 집에서 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# M개의 치킨집만 남기고 모두 폐업시킬 때, 도시의 치킨 거리가 최솟값이 되도록

# 치킨집마다 집과의 거리를 계산해서 가장 가까운 치킨집 거리를 반환
def nearest(house, stores):
    hx, hy = house
    min_distance = float("inf")
    for sx, sy in stores:
        dist = abs(hx - sx) + abs(hy - sy)
        if dist < min_distance:
            min_distance = dist
    return min_distance

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    houses = []
    chickens = []
    # 그래프를 입력받으며 집 위치와 치킨집 위치를 튜플로 저장
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j] == 1:
                houses.append((i, j))
            if line[j] == 2:
                chickens.append((i, j))
        graph.append(line)

    answer = []
    # M개의 치킨집으로 가능한 조합들을 돌며 도시의 치킨 거리들을 저장
    for stores in combinations(chickens, M):
        city_chicken_dist = 0
        for house in houses:
            city_chicken_dist += nearest(house, stores)
        answer.append(city_chicken_dist)
    # 그 중 최솟값 출력
    print(min(answer))