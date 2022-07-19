import sys
from collections import deque

# n, m, v를 공백으로 구분하여 입력받기
n, m, v = map(int, sys.stdin.readline().split())

# graph 만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 내림차순 정렬
for arr in graph:
    arr.sort()

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

# dfs 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# bfs 메서드 정의
def bfs(graph, start, visited):
    # deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        w = queue.popleft()
        print(w, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[w]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)