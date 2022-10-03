# 여기서는 좌표 1부터 시작
# 반복을 돌면서 1에서 bfs해서 2를 발견하면 그 거리 구하고 -> 응. 이거 아니야

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, -> 아? 경우의 수?

house, chicken = [], []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i+1,j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1,j+1))

# print(house)
# print(chicken)

def distance(a,b):
    distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return distance

min_distance = 100000
sum_distance = 0

for chi in combinations(chicken, m):
    for hou in house:
# 않이...여기서... 또 완전탐색..? 이거 맞아?
        sum_distance += min([distance(hou, i) for i in chi])
    min_distance = min(min_distance, sum_distance)
    sum_distance = 0

print(min_distance)

# 엥 이게 시간 초과가 안나?