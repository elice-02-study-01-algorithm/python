# import sys
# input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 다시 돌아올게.. dfs... bye..
# def dfs(x,y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx > 0 and nx <= m and ny > 0 and ny <= n and graph[ny][nx] == 1:
#             graph[ny][nx] = -1
#             dfs(nx,ny)
#     if nx == m and ny == n:
#         return

def bfs(x,y): 
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))