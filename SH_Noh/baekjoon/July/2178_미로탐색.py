from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
# maze에서 1인 곳들 각각에 최단 거리로 도착할 수 있는 칸 수
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 1:
                # 아직 방문하지 않은 칸이거나 현재칸보다 한 칸 더 걸리는 칸
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    print(q)
    
    print(visited)
    return visited[N-1][M-1]

print(bfs(0, 0))

