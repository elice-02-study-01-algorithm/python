'''
강철부대가 위치한 지역을 포함한 총 지역의 수 n,
두 지역을 왕복할 수 있는 길 정보를 담은 2차원 정수 배열 roads,
각 부대원이 위치한 서로 다른 지역들을 나타내는 정수 배열 sources,
강철부대의 지역 destination이 주어졌을 때,
주어진 sources의 원소 순서대로 강철부대로 복귀할 수 있는 최단시간을 담은 배열을 return
복귀가 불가능한 경우 해당 부대원의 최단시간은 -1
'''
# DFS-25점
'''
def solution(n, roads, sources, destination):
    answer = []
    mapInfo ={}
    for a, b in roads:
        try:
            mapInfo[a].append(b)
        except:
            mapInfo[a] = [b]
        
        try:
            mapInfo[b].append(a)
        except:
            mapInfo[b] = [a]
    print(mapInfo)
    
    def DFS(nodeInfo, start, final):
        visited=[]
        stack = [start]
        while stack:
            curNode = stack.pop()
            if curNode not in visited:
                visited.append(curNode)

                if nodeInfo[curNode]:
                    stack += nodeInfo[curNode]
                if final in nodeInfo[curNode]:
                    return visited+[final]
            if visited[-1]==final:
                break
        if visited[-1] != final:
            return []
        return visited
    
    for source in sources:
        answer.append(len(DFS(mapInfo, destination, source))-1)
        
    return answer
'''

# 다익스트라-62.5점
'''
import heapq
INF = int(1e9)
def solution(n, roads, sources, destination):
    answer = []

    mapInfo = [[] for _ in range(n+1)] 
    visited = [False] * (n+1)
    distance = [INF]*(n+1)

    for a, b in roads:
        mapInfo[a].append((b, 1))
        mapInfo[b].append((a, 1))
    
    def getMinNode():
        minVal = INF
        index = 0
        for i in range(1, n+1):
            if not visited[i] and distance[i] < minVal:
                minVal = distance[i]
                index = i
        return index
    
    def dijkstra(start):
        distance[start] = 0
        visited[start] = True

        for i in mapInfo[start]:
            distance[i[0]] = i[1]

        for _ in range(n-1):
            now = getMinNode()
            visited[now] = True

            for next in mapInfo[now]:
                cost = distance[now] + next[1]
                if cost < distance[next[0]]:
                    distance[next[0]] = cost
        
    dijkstra(destination)

    for i in sources:
        if distance[i]==INF:
            answer.append(-1)
        else:
            answer.append(distance[i])
        
    return answer
# 62.5점
'''
# 다익스트라+우선순위큐-100점
import heapq
# 무한
INF = int(1e9)

def solution(n, roads, sources, destination):
    answer = []

    # 지역마다 방문했는지 확인
    visited = [False] * (n+1)
    # destination으로부터 걸리는 거리
    distance = [INF]*(n+1)

    # 지역 개수만큼 그래프 초기화
    mapInfo ={List1: {} for List1 in range(n+1)}
    for a, b in roads:
        mapInfo[a][b] = 1
        mapInfo[b][a] = 1
    # {0: {}, 1: {2: 1}, 2: {1: 1, 3: 1}, 3: {2: 1}}
    # {0: {}, 1: {2: 1, 4: 1}, 2: {1: 1, 4: 1, 5: 1}, 3: {}, 4: {1: 1, 2: 1, 5: 1}, 5: {2: 1, 4: 1}}
    
    # 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신한다(≒BFS)
    def dijkstra(start):
        distance[start] = 0
        visited[start] = True

        queue = []
        # 가장 짧은 거리를 가진 노드 정보를 꺼내기 위해 우선순위큐 사용
        heapq.heappush(queue, [distance[start], start])

        while queue:

            curDist, curNode = heapq.heappop(queue)
            # 첫 정점에 인접한 노드들의 각각에 대해
            # 첫 정점에서 각 노드로 가는 거리와 
            # 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교
            if distance[curNode] < curDist:
                continue
            # 만약 배열에 저장되어 있는(distance[curNode])것보다
            # 첫 정점에서 해당 노드로 가는 거리가 더 짧은 경우 업데이트
            for adjacent, weight in mapInfo[curNode].items():
                distanceNow = curDist + weight
                if distanceNow < distance[adjacent]:
                    distance[adjacent] = distanceNow
                    heapq.heappush(queue, [distanceNow, adjacent])
        
    dijkstra(destination)

    for i in sources:
        # 아무것도 업데이트되지 않았다면(=INF) 갈 수 없는 경로
        if distance[i]==INF:
            answer.append(-1)
        else:
            answer.append(distance[i])
        
    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1)) # [1, 2]
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)) #[2, -1, 0]
