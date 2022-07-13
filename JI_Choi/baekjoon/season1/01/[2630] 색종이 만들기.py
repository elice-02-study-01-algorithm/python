N = int(input())
confetti = [list(map(int, input().split())) for _ in range(N)]
P = [0,0] # 색종이에 대한 기준점
count = [0,0] # 각각 white, blue 색종이의 수

# 색종이 색상을 확인하기 위해 필요한 기준점들을 생성
# 이후 기준점과 길이(n)를 이용하여 for문으로 색상을 확인할 예정
def points(p, n):
  a = p[0]
  b = p[1]
  if n == 0:
    return [[a,b]]
  else:
    return [[a,b], [a+n,b], [a,b+n], [a+n,b+n]]

# 입력되는 색종이(m)에 대한 전체 원소들의 합
def sumAll(m):
  acc = 0
  for i in m:
    acc += sum(i)
  return acc

# 같은 색상인 사각형의 개수를 세는 함수
# 기준점(p), 색종이(m), sub 색종이의 한 변의 길이(n) 입력
def countSquare(p, m, n):
  global count
  pointList = points(p, n//2)
  
  # 처음 주어진 색종이가 흰색(0)인 경우
  if sumAll(m) == 0:
    count[0] = 1
    return
  
  # 처음 주어진 색종이가 파란색(1)인 경우
  elif sumAll(m) == n**2:
    count[1] = 1
    return
  
  else:
    for point in pointList:
      # 이중 for문을 정지시키기 위한 장치
      isItBreak = False
      for i in range(n//2):
        if isItBreak == True:
          break
        for j in range(n//2):
          # 첫 원소의 색상을 저장
          # 확인하는 범위에 다른 색상이 존재하는지 확인
          # 다른 색상이 존재하는 경우, break 후 pointList에서 다른 point를 선택
          firstColor = m[point[0]][point[1]]
          if m[point[0]+i][point[1]+j] != firstColor:
            countSquare(point, m, n//2)
            isItBreak = True
            break

      # 확인하는 범위의 색상이 모두 같은 경우, 그 색상의 색종이 개수를 하나 추가
      if isItBreak == False:
        count[firstColor] += 1

  return

## 같은 색상인 색종이 개수 확인 ##
countSquare(P, confetti, N)
print(count[0])
print(count[1])
