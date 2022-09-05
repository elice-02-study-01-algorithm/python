# 운전할 거리의 최솟값 구하기
import heapq
from sys import stdin
input = stdin.readline

shortcutCount, highwayLong = map(int, input().split())
graph = [[] for _ in range(highwayLong+1)]
for i in range(highwayLong):
    graph[i].append((i+1, 1))

for i in range(shortcutCount):
    start, end, length = map(int, input().split())
    if end > highwayLong: continue
    graph[start].append((end, length))

distance = [float('inf')] * (highwayLong + 1)
distance[0] = 0

queue = []
heapq.heappush(queue, (0, 0))
while queue:
    dst, cur = heapq.heappop(queue)
    if distance[cur] < dst:
        continue
    for x in graph[cur]:
        cost = dst + x[1]

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(queue, (cost, x[0]))
# print(distance)
print(distance[highwayLong])