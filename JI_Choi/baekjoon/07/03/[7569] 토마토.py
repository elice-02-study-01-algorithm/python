from sys import stdin
from collections import deque

# m(가로), n(세로), h(높이)를 공백으로 구분하여 입력받기
m, n, h = map(int, stdin.readline().split())

# 3차원 graph 만들기
graph = []
# deque 라이브러리 사용
queue = deque()

# 높이의 길이만큼 반복
for k in range(h):
    layer_data = []
    # 세로의 길이만큼 반복
    for j in range(n):
        row_data = list(map(int, stdin.readline().split()))
        layer_data.append(row_data)
        # 가로의 길이만큼 반복
        for i in range(m):
            if layer_data[j][i] == 1:
                queue.append((i, j, k))

    # h층에 해당하는 정보를 graph에 저장
    graph.append(layer_data)

# 이동할 여섯 방향 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# BFS 소스코드 구현


def bfs():
    # 큐가 빌 때 까지 반복
    while queue:
        x, y, z = queue.popleft()
        # 현재 위치에서 여섯 방향으로의 위치 확인
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 공간을 벗어나지 않고, 해당 노드를 처음 방문하는 경우
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and graph[nz][ny][nx] == 0:
                queue.append((nx, ny, nz))
                graph[nz][ny][nx] = graph[z][y][x]+1


bfs()

# 모두 익을 때까지 며칠이 걸리는지 확인


def days():
    ans = 0
    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit(0)
            ans = max(ans, max(j))
    print(ans-1)


days()
