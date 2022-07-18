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
                q.append([i, j, k])
    boxes.append(temp)

# 위아래 오른왼
dir_x = [0, 0, 1, -1, 0, 0]
dir_y = [-1, 1, 0, 0, 0, 0]
dir_z = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        # 1인 좌표
        cur = q.popleft()
        # 방향을 더해주면서
        for i in range(6):
            cur_x = cur[0] + dir_x[i]
            cur_y = cur[1] + dir_y[i]
            cur_z = cur[2] + dir_z[i]
        if cur_x < 0 or cur_y < 0 or cur_z < 0 or cur_x >= n or cur_y >= m or cur_z >= h:
            return
        if boxes[cur_z][cur_x][cur_y] == 0:
            q.append([cur_z, cur_x, cur_y])
            boxes[cur_z][cur_x][cur_y] = boxes[cur[0]][cur[1]][cur[2]] + 1
            

bfs()
result = 0
print(boxes)
for i in boxes:
    for row in i:
          for col in row:
              if col == 0:
                  print(-1)
                  exit()
              result = max(result, max(row))
print(result - 1)

# 실패!