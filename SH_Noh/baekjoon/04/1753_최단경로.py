# 서로 다른 두 정점 사이에 여러 개의 간선 존재 가능
# 최단 경로의 경로값을 출력, 경로가 존재하지 않으면 INF 출력

import heapq
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

node, line = map(int, input().split())
startNode = int(input())
graph = [[] for _ in range(node+1)]
for _ in range(line):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
distance = [INF for _ in range(node+1)]

queue = []
def dijkstra(startNode):
    heapq.heappush(queue, (0, startNode)) # 시작점은 거리 0
    distance[startNode] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            # next는 (end, cost)로 append 해놓은 정보
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))

dijkstra(startNode)
for i in range(1, node+1):
    print("INF" if distance[i] == INF else distance[i])