# 예제 1, 2는 통과하지만 예제 3은 통과 못하는 코드
# 문제가 되는 상황
# 지름길로 가는 길 사이 일반 길로 가는 경우가 0으로 시작하거나
# highwayD로 끝나는 경우가 아니면 최단 거리 못 잡아내는 문제 발생

# 다익스트라 알고리즘
def getShortest(graph, start, end):
    V = len(graph)
    visited = [False for _ in range(V)]

    dist = [float('inf') for _ in range(V)]
    dist[start] = 0
    while True:
        minimum = float('inf')
        node = -1
        for j in range(V):
            if not visited[j] and minimum > dist[j]:
                minimum = dist[j]
                node = j
        if minimum == float('inf'): break
        visited[node] = True

        for j in range(len(graph[node])):
            des = graph[node][j][0]
            cost = graph[node][j][1]
            if dist[des] > dist[node]+cost:
                dist[des] =dist[node]+cost
    return dist[end]


shortestN, highwayD = map(int, input().split())
wayGraph = []
# 정점 수 세기 위한 리스트
dotNum = []
for _ in range(shortestN):
    start, end, far = map(int, input().split())
    # 고속도로 끝점이 종착을 넘어설 때 어차피 쓰지 않으므로 버리기
    if end > highwayD: continue
    dotNum.append(start)
    dotNum.append(end)
    wayGraph.append([start, end, far])

wayGraph.sort(key=lambda x:x[0])

# 일반 도로를 간선으로 하는 정점 추가 위한 리스트
addGraph = []
for info in wayGraph:
    # 0에서 지름길 시작하는 것까지 추가
    if info[0] != 0:
        addGraph.append((0, info[0], info[0]))
    # 지름길 끝나는 부분에서 종착점까지 추가
    if info[1]<highwayD and info[1] != highwayD:
        addGraph.append((info[1], highwayD, highwayD-info[1]))
# 중복 제거 위한 집합 처리
finGraph = wayGraph+addGraph
setGraph = set(finGraph)
finGraph = list(setGraph)
finGraph.sort(key=lambda x:(x[0], x[1]))

# 정점 중복 제거 위한 집합 처리
setDotNum = set(dotNum)
dotNum = list(setDotNum)
dotN = len(dotNum)

# 정점을 인덱스로 갖는 그래프 제작
processedGraph = [[] for _ in range(highwayD+1)]

for info in finGraph :
    print(info)
    processedGraph[info[0]].append((info[1], info[2]))
    processedGraph[info[1]].append((info[0], info[2]))
# 450 0 = 450
# 9 40 15 10 100 260 = 434
# 9 40 15 70 28 270 = 134 298 432
#print(processedGraph)

print(getShortest(processedGraph, 0, highwayD))
#----------------------------------------------------

# 답안 코드
shortestN, highwayD = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(shortestN)]

# 정점별로 최단 거리 기록할 리스트
dist = [ i for i in range(highwayD+1)]

for i in range(highwayD+1):
    if i > 0:
        # 바로 직전 정점에서 1 더한 것과 비교했을 때 들어오는 게 더 적으면 바꿔치기
        dist[i] = min(dist[i], dist[i-1]+1)
    # 지름길 시작점~끝점이 고속도로 범위내 and 해당 지름길로 갔을 때 더 작으면 바꿔치기
    for start, end, far in graph:
        if i == start and end <= highwayD and dist[i]+far < dist[end]:
            dist[end] = dist[i] +far
print(dist[highwayD])
