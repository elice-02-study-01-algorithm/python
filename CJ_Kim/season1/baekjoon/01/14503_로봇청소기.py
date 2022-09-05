row, col = input().split()
currentR, currentC, currentD = input().split()

# 입력받은 좌료를 2차원 배열로 생성
# 예시: roomMap = [
# [1, 1, 1],
# [1, 0, 1],
# [1, 1, 1]
# ]
currentRoomMap = []
for _ in range(int(row)):
  currentRoomMap.append(list(map(int, input().split())))

# d/방향/(dr, dc): 0/북/(-1, 0), 1/동/(0, 1), 2/남/(1, 0), 3/서/(0, -1)
#    -1
# -1 기준 +1
#    +1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 바라보는 방향이 왼쪽으로 회전하는 경우/cf. 오른쪽인 경우 (d+1)%4
def getD_rotateLeft(d):
  return (d+3)%4
# 바라보는 방향에서 후진하는 경우==현재 위치의 반대 방향으로 한 칸 이동
def getD_goBack(d):
  return (d+2)%4

def getCountRobotVaccuum(r, c, d, roomMap):
  countCleaned = 1
  # 청소 완료 시 2로 변경
  roomMap[r][c] = 2
  # 청소한 위치와 방향을 queue에 저장
  queue = list([[r, c, d]])
  #print('first', queue)

  while queue:
    r, c, d = queue.pop(0)
    temp_d = d

    for i in range(4):
      # 현재 위치에서 바로 왼쪽의 공간 확인하기
      temp_d = getD_rotateLeft(temp_d)
      newR, newC = r+dr[temp_d], c+dc[temp_d]

      # 영역 내, 청소하지 않은 부분일 경우
      if 0 <= newR < int(row) and 0 <= newC < int(col) and roomMap[newR][newC] == 0:
        countCleaned += 1
        roomMap[newR][newC] = 2
        queue.append([newR, newC, temp_d])
        #print('cleanfirst', queue)
        break
      # 2a번 단계가 연속으로 네 번 실행되었을 경우
      elif i == 3:
        newR, newC = r+ dr[getD_goBack(d)], c + dc[getD_goBack(d)]
        queue.append([newR, newC, d])
        #print('cleanyet', queue)
        # 뒤쪽이 벽이라면
        if roomMap[newR][newC] == 1:
          #print('final', queue)
          return countCleaned

print(getCountRobotVaccuum(int(currentR), int(currentC), int(currentD), currentRoomMap))