from collections import deque
from sys import stdin
input = stdin.readline

# 4개 이상의 뿌요가 모이면 터진다!
# 여러 그룹이 있으면 동시에 터지고 이후 상황에서 터지면 콤보가 쌓인다!
def PuyoPop(i, j):
    global trigger
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 1
    puyo = [(i, j)]
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == False:
                # 상하좌우의 같은 색 뿌요 찾기
                if state[x][y] == state[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
                    puyo.append((nx, ny))
    
    if count >= 4:
        # 뿌요가 한 번이라도 터지면 콤보!
        trigger = True
        # 뿌요를 터뜨리는 함수 돌리기
        for px, py in puyo:
            state[px][py] = "."


# 중력에 의해 떨어지는 뿌요!
def PuyoDrop(state):
    for j in range(6):
        q = deque([])
        for i in range(11, -1, -1):
            # 한 줄에 남아있는 뿌요들만 모으기
            if state[i][j] != '.':
                q.append(state[i][j])
        # 바닥부터 차례로 채워주고 남는 공간은 .으로 채우기
        for i in range(11, -1, -1):
            if q:
                state[i][j] = q.popleft()
            else:
                state[i][j] = "."


state = [list(input().strip()) for _ in range(12)]
trigger = True

if __name__ == "__main__":
    combo = 0
    while trigger == True:
        trigger = False
        visited = [[False] * 6  for _ in range(12)]
        for i in range(11, -1, -1):
            for j in range(6):
                if visited[i][j] == False and state[i][j] != ".":
                    # 현상황에서 터뜨리는 함수 돌리기
                    PuyoPop(i, j)
        # print("")
        # for i in range(12):
        #     print("".join(state[i]))
        # print("=================")

        # 한 번이라도 터졌으면 콤보 올리고 빈 칸 채우기 
        if trigger == True:
            combo += 1
            PuyoDrop(state)
         
        # for i in range(12):
        #     print("".join(state[i]))
        # print("=================")

    print(combo)

# 문제가 된 예제
# ......
# ......
# ......
# ......
# ......
# ......
# .G....
# RR....
# RY....
# RYG...
# RRY...
# RYYGG.