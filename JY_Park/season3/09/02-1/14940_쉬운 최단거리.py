import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]

graph = []
for i in range(n):
    temp1 = list(map(int, input().split()))
    for j in range(m):
        if temp1[j] == 2:
            cur = (i,j)
            break
    graph.append(temp1)


visited = []
for i in range(n):
    temp2 = []
    for j in range(m):
        if graph[i][j] == 0:
            temp2.append(True)
        else: temp2.append(False) 
    visited.append(temp2)


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(i,j):
    queue = deque([(i,j)])
    graph[i][j] = 0
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                visited[nx][ny] = True
            elif nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                visited[nx][ny] = True
    return

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 2:
#             cur = (i,j)
#             break
bfs(cur[0], cur[1])

# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            graph[i][j] = -1

for i in graph:
    print(*i)


# 원래 못가는 땅이면 visited True
'''
[반례]
못 가는 땅이 0이면 그대로 0, 1이면 -1을 출력해야 되지만, 위 코드는 무조건 -1을 출력하기 때문에 틀립니다.

[Input]
2 2
2 0
0 0

[Output]
0 0
0 -1

[Answer]
0 0
0 0
'''