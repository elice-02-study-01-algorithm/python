# 1은 익은 토마토 / 0은 익지 않은 토마토 / -1은 토마토가 들어있지 않은 칸
from collections import deque
from sys import stdin
input = stdin.readline

M, N, H = map(int, input().split())
# 토마토 박스 상태 3차원 배열
array = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

q = deque()
def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                # 익은 토마토의 다음 칸의 토마토를 익힘
                # 이미 익은 토마토여도 계속 더해지는게 포인트!
                if array[nz][nx][ny] == 0:
                    array[nz][nx][ny] = array[z][x][y] + 1
                    q.append((nz, nx, ny))

for i in range(H):
    for j in range(N):
        for k in range(M):
            # 익은 토마토들이 있는 위치를 q에 추가
            if array[i][j][k] == 1:
                q.append((i, j, k))

bfs()
# print(array)

day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 끝까지 익지 않은 토마토가 있다면 -1 출력
            if array[i][j][k] == 0:
                print(-1)
                exit()
            day = max(day, array[i][j][k])

# 최대값은 처음부터 익어있던 토마토 중에 나오기 때문에 1을 빼줘야 함
print(day - 1)
