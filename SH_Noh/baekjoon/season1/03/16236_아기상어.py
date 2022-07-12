# 처음 아기상어 크기는 2
# 1초에 상하좌우로 한 칸씩 이동
# 자기보다 큰 물고기가 있는 칸은 지나갈 수 없음
# 자기보다 작은 크기의 물고기만 먹을 수 있음
# 자기랑 같은 크기면 지나갈수만 있음
# 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
# 먹을 수 있는 물고기가 1마리 이상이면 가까운 물고기를 먹으러 감
    # 최소 거리 물고기가 여러 마리면 가장 위에 있는 물고기
        # 또 여러 마리면 가장 왼쪽에 있는 물고기를 먹음
# 더이상 먹을 수 있는 물고기가 공간에 없을 때 끝

from sys import stdin
input = stdin.readline

def eatFish(x, y, sharkSize):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = [(x, y)]
    visited[x][y] = 1
    tmp = []
    for curX, curY in queue:
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if space[nx][ny] <= sharkSize:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[curX][curY] + 1
                    if space[nx][ny] < sharkSize and space[nx][ny] != 0:
                        tmp.append((nx, ny, distance[nx][ny]))
    return sorted(tmp, key = lambda x: (-x[2], -x[0], -x[1]))
        

if __name__ == "__main__":
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    fish = 0
    x, y, size = 0, 0, 2
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                x = i
                y = j

    count = 0
    result = 0
    while True:
        fishInfo = eatFish(x, y, size)
        if len(fishInfo) == 0:
            break
        nx, ny, dist = fishInfo.pop()
        
        result += dist
        space[x][y], space[nx][ny] = 0, 0

        x, y = nx, ny
        count += 1
        if count == size:
            size += 1
            count = 0

    print(result)

# https://resilient-923.tistory.com/357