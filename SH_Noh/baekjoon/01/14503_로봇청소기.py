import sys

N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
coordinate = []
for _ in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().strip().split())))
isVisited = [([False] * M) for _ in range(N)]
isVisited[r][c] = True # 현재 위치 방문

# 0: 위쪽 이동, 1: 오른쪽 이동, 2: 아래 이동, 3: 왼쪽 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned = 1 # 현재 위치 항상 청소하고 시작
turnTime = 0 # 왼쪽으로 회전한 횟수

while True:
    # 0 : 북, 1 : 동, 2 : 남, 3 : 서
    d = (d - 1) % 4 # 왼쪽으로 회전
    nx = r + dx[d] # 회전한 방향으로 이동
    ny = c + dy[d] # 회전한 방향으로 이동
    
    if isVisited[nx][ny] == 0 and coordinate[nx][ny] == 0: # 이동을 했는데 방문하지 않았고 빈 공간인 경우
        isVisited[nx][ny] = True # 방문 처리
        cleaned += 1 # 청소 횟수 증가
        turnTime = 0 # 왼쪽 방향 회전 횟수 0으로 초기화
        r = nx # 위치 이동
        c = ny # 위치 이동
        continue # 반복
    else: # 이동이 불가능 한 경우 왼쪽 방향 회전 횟수만 증가
        turnTime += 1

    if turnTime == 4: # 총 4번 회전 한 경우, 네 방향 모두 청소가 되어 있거나 벽이 있는 경우
        nx = r - dx[d] # 뒤로 이동
        ny = c - dy[d] # 뒤로 이동

        if coordinate[nx][ny] == 0: # 이동한 위치가 벽이 아니라면
            r = nx # 이동
            c = ny # 이동
        else: # 그렇지 않으면
            break # 작동을 멈춤
        turnTime = 0 # 왼쪽 방향 회전 횟수 초기화

print(cleaned) # 청소 횟수 출력