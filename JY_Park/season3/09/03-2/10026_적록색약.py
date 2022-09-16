# 리팩토링 전 : bfs로 돌면서 1과 0으로 graph 값 업데이트.

'''
from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
dx, dy = (0,1,0,-1), (1,0,-1,0)


def bfs(i,j):
    queue = deque([(i,j)])
    cur = graph[i][j]

    if cur == 'B':
        graph[i][j] = 0
    else: graph[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and cur == graph[nx][ny]:
                if cur == 'B':
                    graph[nx][ny] = 0
                else: graph[nx][ny] = 1
                queue.append((nx,ny))

# 적록색약 bfs
def bfs_RG(i,j):
    queue = deque([(i,j)])
    cur = graph[i][j]
    graph[i][j] = 2

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and cur == graph[nx][ny]:
                graph[nx][ny] = 2
                queue.append((nx,ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] in ["B","R","G"]:
            cnt += 1
            bfs(i,j)
print(graph)
# 적록색약 bfs
cnt2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] in [0,1]:
            cnt2 += 1
            bfs_RG(i,j)

print(cnt, cnt2)

'''

# 리팩토링 bfs 코드가 반복됨.

from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx, dy = (0,1,0,-1), (1,0,-1,0)

def bfs(i,j):
    queue = deque([(i,j)])
    cur = graph[i][j]

    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and cur == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))

def colorBlindness():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "G":
                graph[i][j] = "R"

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            bfs(i,j)

colorBlindness()

# visited 초기화
visited = [[False]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt2 += 1
            bfs(i,j)

print(cnt, cnt2)