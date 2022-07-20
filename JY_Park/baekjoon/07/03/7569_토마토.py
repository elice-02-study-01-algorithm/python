from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int,input().split())

dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
graph = []
for i in range(h):
    pre = []
    for j in range(n):
        pre.append(list(map(int, input().split())))
        for k in range(m):
            if pre[j][k] == 1:
                queue.append((k,j,i))
    graph.append(pre)

# print(graph)


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx >= 0 and ny >= 0 and nz >= 0 and nx < m and ny < n and nz < h and graph[nz][ny][nx] == 0:
                queue.append((nx,ny,nz))
                graph[nz][ny][nx] = graph[z][y][x] + 1

bfs()
# print(graph)


# 최소 일수를 구하기
result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
            if k > result:
                result = k
print(result-1)

# 반례 (답2)

# 5 3 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0