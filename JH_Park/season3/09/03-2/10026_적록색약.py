from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [[False] * n for _ in range(n)]
zone = [list(input()) for _ in range(n)]
queue = deque()
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            if 0 <= cur_x < n and 0 <= cur_y < n and not visited[cur_x][cur_y] and zone[cur_x][cur_y] == zone[x][y]:
                queue.append([cur_x, cur_y])
                visited[cur_x][cur_y] = True

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j)
            count += 1
print(count, end=' ')

# 적록색약인 사람을 위해 R 과 G 둘을 같게 해줘야겠지?
for i in range(n):
    for j in range(n):
        if zone[i][j] == 'R':
            zone[i][j] = 'G'
# 앞서 visited에 변경이 있었으므로 초기화 해준다
count = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j)
            count += 1
print(count)