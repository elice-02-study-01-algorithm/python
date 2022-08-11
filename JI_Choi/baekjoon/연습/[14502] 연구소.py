from sys import stdin
from collections import deque
import copy

# 세로 길이, 가로 길이 각각 입력받기
n, m = map(int, stdin.readline().split())

# 그래프 선언
graph = []

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전 영역의 개수 선언
safe_zone = 0

# bfs 메서드 정의
def bfs():
    # deque 라이브러리 사용
    queue = deque()
    # 깊은 복사
    tmp_graph = copy.deepcopy(graph)
    # queue에 바이러스가 존재하는 좌표값 담기
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 처음 방문하는 경우
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))
    
    global safe_zone
    # count 초기화
    count = 0
    # 안전 영역 개수 세기
    for i in range(n):
        count += tmp_graph[i].count(0)

    # 안전 영역의 최대 개수
    safe_zone = max(safe_zone, count)


# (1)벽을 만들고 (2)안전 영역의 개수를 세는 메서드
def build_walls(count):
    # count가 3인 경우 (안전 영역의 개수 세기)
    if count == 3:
        # bfs 메서드 실행
        bfs()
        return
    
    # count가 3보다 작은 경우 (벽 만들기)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                # count + 1에 대해 재귀적 실행
                build_walls(count + 1)
                # 이건 왜 있는거지????????
                graph[i][j] = 0


# 그래프 입력받기
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))


build_walls(0)
print(safe_zone)