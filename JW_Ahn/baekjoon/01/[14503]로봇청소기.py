# 세로 크기 N, 가로 크기 M
# 좌표 (r, c) 바라보는 방향 d
N, M = map(int, input().split())
x, y, d = map(int, input().split())

# 지도 입력받기
input_map = []
for i in range(N) :
  input_map.append(list(map(int, input().split())))

# 처음 입력받은 곳 청소 완료
input_map[x][y] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향으로 회전하는 함수
def turn_left(d) :
  return (d + 3) % 4

# 청소하는 칸 개수
# 회전 횟수
clean_cnt = 1
turn_cnt = 0

while True :
  d = turn_left(d)
  nx = x + dx[d]
  ny = y + dy[d]
  
  if 0 <= nx <= N and 0 <= ny <= M and input_map[nx][ny] == 0 :
    input_map[nx][ny] = 2
    clean_cnt += 1
    x, y = nx, ny
    turn_cnt = 0
    # print("clean :", *input_map, sep="\n")
    continue
  else :
    turn_cnt += 1
  
  # 네 번 회전했을 경우, 한 칸 후진 => 뒤가 벽이라면 멈춤. 아니라면 청소
  if turn_cnt == 4 :
    nx = x - dx[d]
    ny = y - dy[d]
    
    if input_map[nx][ny] == 1 :
      break
    else :
      x, y = nx, ny
    
    turn_cnt = 0

print(clean_cnt)