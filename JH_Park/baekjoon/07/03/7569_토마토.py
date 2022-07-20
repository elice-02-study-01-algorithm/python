from collections import deque
m, n, h = map(int, input().split())
boxes = []
q = deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append((k, j, i))
    boxes.append(temp)
# 위아래 오른왼
dir_x = [1, 0, -1, 0, 0, 0]
dir_y = [0, -1, 0, 1, 0, 0]
dir_z = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        # 1인 좌표
        cur_x, cur_y, cur_z = q.popleft()
        # 방향을 더해주면서
        for i in range(6):
            move_x = cur_x + dir_x[i]
            move_y = cur_y + dir_y[i]
            move_z = cur_z + dir_z[i]
            if 0 <= move_x < m and 0 <= move_y < n and 0 <= move_z < h and boxes[move_z][move_y][move_x] == 0:
                q.append((move_x, move_y, move_z))
                boxes[move_z][move_y][move_x] = boxes[cur_z][cur_y][cur_x] + 1
            

bfs()

result = 0
for i in boxes:
    for row in i:
          for col in row:
              if col == 0:
                  print(-1)
                  exit()
              # result = max(result, max(row))
              if col > result:
                  result = col
print(result - 1)