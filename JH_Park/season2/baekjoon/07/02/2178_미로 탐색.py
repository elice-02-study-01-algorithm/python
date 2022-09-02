import math

#아래 위 오른쪽 왼쪽
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
miro = [list(map(int, input())) for i in range(n)]
bool_miro = [[True] * m for i in range(n)]
bool_miro[0][0] = False
min_count = math.inf

# 계속 호출 될 함수
def dfs(x, y, count):
    # 아예 미로에서 벗어나면
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    # 미로 끝에 도착하면
    if x == n - 1 and y == m - 1:
        global min_count
        if min_count > count:
            min_count = count
            return
    # 미로를 탐방중!
    for i in range(4):
        dir_x = x + dx[i]
        dir_y = y + dy[i]
        # 내가 이 길을 갈 수 있는지 체크한다. 그리고 지나갔던 길인지 여부를 체크한다.
        if dir_x >= n or dir_y >= m:
            continue
        if miro[dir_x][dir_y] == 1 and bool_miro[dir_x][dir_y] == True:
            bool_miro[dir_x][dir_y] = False
            dfs(dir_x, dir_y, count + 1)
            # 갔던 길을 되돌아 오면 다시 True
            bool_miro[dir_x][dir_y] = True
            
dfs(0, 0, 1)
print(min_count)