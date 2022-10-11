from collections import deque
from sys import stdin
input = stdin.readline

def BFS(x, y, graph, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if graph[cx][cy] == graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def colorChange(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "G":
                graph[i][j] = "R"
    return graph

if __name__ == "__main__":
    N = int(input())
    graph = [list(input().strip()) for _ in range(N)]
    
    visited = [[False] * N for _ in range(N)]
    normal = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                BFS(i, j, graph, visited)
                normal += 1
    
    graph = colorChange(graph)
    visited = [[False] * N for _ in range(N)]
    colorless = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                BFS(i, j, graph, visited)
                colorless += 1

    print(normal, colorless)