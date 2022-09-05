from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result_map = [list(map(int, input().split())) for _ in range(n)]
# 다음과 같은 경로로 이동합니다.
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and result_map[nx][ny] == 1:
                q.append((nx, ny))
                result_map[nx][ny] = result_map[x][y]+1

# 2를 찾습니다.
for i in range(n):
    for j in range(m):
        if result_map[i][j] == 2:
            q.append((i, j))
            break
bfs()
for i in range(n):
    for j in range(m):
        goal = result_map[i][j]
        print((goal - 2 if goal else 0), end=" ")
    print()