from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [input().split() for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "0":
            answer[i][j] = 0
        # 목표 지점
        elif graph[i][j] == "2":
            tr, tc = i, j

q = deque([[tr, tc, 0]])
answer[tr][tc] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    current = q.popleft()
    cr, cc, cnt = current
    if not visit[cr][cc]:
        visit[cr][cc] = True
        for d in range(4):
            nr = cr + dx[d]
            nc = cc + dy[d]
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc]:
                if graph[nr][nc] == "1":
                    answer[nr][nc] = cnt + 1
                    q.append([nr, nc, cnt + 1])

for i in range(n):
    print(*answer[i])