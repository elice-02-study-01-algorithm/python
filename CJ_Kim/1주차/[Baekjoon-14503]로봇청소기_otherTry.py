# 다른 점은 입력받은 변수들을 map 함수로 감싼 것
# 근소하게 시간을 줄여서 흥미롭다
# count 함수를 따로 뺀 것은 시간 차이 없음
row, col = map(int, input().split())
currentR, currentC, currentD = map(int, input().split())

currentRoomMap = []
for _ in range(row):
  currentRoomMap.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def getD_rotateLeft(d):
  return (d+3)%4

def getD_goBack(d):
  return (d+2)%4

def getCountRobotVaccuum(r, c, d, roomMap):

  roomMap[r][c] = 2
  queue = list([[r, c, d]])

  while queue:
    r, c, d = queue.pop(0)
    temp_d = d

    for i in range(4):
      temp_d = getD_rotateLeft(temp_d)
      newR, newC = r+dr[temp_d], c+dc[temp_d]

      if 0 <= newR < row and 0 <= newC < col and roomMap[newR][newC] == 0:
        roomMap[newR][newC] = 2
        queue.append([newR, newC, temp_d])
        break

      elif i == 3:
        newR, newC = r+ dr[getD_goBack(d)], c + dc[getD_goBack(d)]
        queue.append([newR, newC, d])

        if roomMap[newR][newC] == 1:
          return

def countTwo(roomMap):
  countNum = 0
  for i in roomMap:
    countNum += i.count(2)
  return countNum

getCountRobotVaccuum(currentR, currentC, currentD, currentRoomMap)
print(countTwo(currentRoomMap))