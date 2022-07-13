from sys import stdin
from collections import deque

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, stdin.readline().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    input_data = list(map(int, stdin.readline().strip()))
    graph.append(input_data)

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 메서드 정의
def bfs(x, y):
    # deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽인 경우
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    # 도착 지점까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))