N = int(input())
confetti = [list(map(int, input().split())) for _ in range(N)]
P = [0,0]
count = [0,0]

# 색종이를 체크하기 위해서 필요한 기준점(point)들을 만드는 함수
def points(p,n):
  a = p[0]
  b = p[1]
  c = int(n//2)
  if c == 0:
    return [[a, b]]
  else:
    return [[a,b], [a+c,b], [a,b+c], [a+c,b+c]]

# 처음 주어진 색종이의 전체 원소의 합
# (처음에 주어진 색종이가 한가지 색상인 경우를 다루기 위해 사용)
def sumAll(m):
  acc = 0
  for elem in m:
    acc += sum(elem)
  return acc

# 사각형 범위를 세는 함수
def countSquare(p, m, n):
  global count
  # 한변의 n/2에 대한 기준점들을 구한다
  pointList = points(p, n)

  # 범위의 길이가 1인 경우
  if n == 1:
    color = m[p[0]][p[1]]
    count[color] += 1

  # 처음 주어진 색종이가 흰색인 경우 (최초의 경우에만 의미있음)
  elif sumAll(m) == 0:
    count[0] = 1

  # 처음 주어진 색종이가 파란색인 경우 (최초의 시작에만 의미있음)
  elif sumAll(m) == n**2:
    count[1] = 1

  # 길이가 8인 정사각형이 주어지면, 길이가 4인 정사각형 4개로 나누어 확인하는 식으로 작동
  # 주어진 범위의 모든 점이 같은 색이면, 색상 카운트에 +1
  else:
    for point in pointList:
      isItBreak = False
      halfLength = (n//2)
      for i in range(halfLength):
        if isItBreak == True:
          break

        for j in range(halfLength):
          color = m[point[0]][point[1]]
          if m[point[0]+i][point[1]+j] != color:
            countSquare(point, m, halfLength)
            isItBreak = True
            break

      if isItBreak == False:
        count[color] += 1

countSquare(P, confetti, N)
print(count[0])
print(count[1])