# 13%까지 겨우 갔는데 시간초과
# 엘리스 강의에서 배운대로 그대로 써먹었지만 실패
'''
from sys import stdin
vertex, line = map(int, stdin.readline().split())
startV = int(stdin.readline())

graph = [[] for _ in range(vertex+1)]
for _ in range(line):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

def getShortest(graph, start):
    lenG = len(graph)
    visited = [False for _ in range(lenG)]
    
    dist = [float('inf') for _ in range(lenG)]
    dist[start] = 0

    while True:
        minimum = float('inf')
        node = -1
        for j in range(lenG):
            if not visited[j] and minimum > dist[j]:
                minimum = dist[j]
                node = j
        if minimum == float('inf'): break
        visited[node] = True

        for j in range(len(graph[node])):
            des = graph[node][j][0]
            cost = graph[node][j][1]

            if dist[des] > dist[node] + cost:
                dist[des] = dist[node] + cost
    return dist

resultList = getShortest(graph, startV)
for i in range(1, vertex+1):
    result = resultList[i]
    if result == float('inf'):
        print('INF')    
    else:
        print(result)
'''
# 시간초과를 막기 위해 다른 자료구조를 이용
from sys import stdin
import heapq

vertex, line = map(int, stdin.readline().split())
startV = int(stdin.readline())

# graph를 index를 시작 vertex로 가지는 2차원 리스트로 구현
graph = [[] for _ in range(vertex+1)]
for _ in range(line):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

dist = [float('inf') for _ in range(vertex+1)]

def getShortestHQ(graph, start):
    
    q = []
    # q에다가 (0, start)를 푸시!
    heapq.heappush(q, (0, start))
    # q = [(0, start)]
    dist[start] = 0

    while q:
        # 가장 작은 항목 pop, 최단 거리 측정하는 node == current
        distance, current = heapq.heappop(q)
        # 가장 작은 항목의 거리가 최단거리 누적보다 멀 때 다음 반복으로 넘어가기
        if dist[current] < distance: continue

        # 그래프에서 current에서 뻗어나가는 vertex들 가지고
        for i in graph[current]:
            # 기록해 둔 최단 거리 누적에다가 가중치를 더해서
            cost = dist[current] + i[1]
            # 만약 그 값이 그 방향에 이미 있는 최단 거리 누적보다 작으면
            if cost < dist[i[0]]:
                # 바꿔치기!
                dist[i[0]] = cost
                # 그 다음에 우선순위큐에다가 다음에 검사할 거 넣어주기
                heapq.heappush(q, (cost, i[0]))

getShortestHQ(graph, startV)
# print(dist) # ex. [inf, 0, 2, 3, 5, inf]

for i in range(1, vertex+1):
    result = dist[i]
    if result == float('inf'):
        print('INF')
        continue
    else:
        print(result)

