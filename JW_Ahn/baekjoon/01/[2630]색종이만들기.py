import sys

def cut_paper(x, y, N): 
  global white, blue
  sum = 0
  
  # 나눠진 부분을 돌아다니며 다 더하기
  for i in range(x, x + N) :
    for j in range(y, y + N) :
      if paper[i][j] :
        sum += 1
  
  newN = N // 2
  # 합이 0이라면 white++ / N * N이라면 blue++ / 다 아니라면 재귀      
  if not sum :
    white += 1
  elif sum == N * N :
    blue += 1
  else :
    cut_paper(x, y, newN)
    cut_paper(x, y+newN, newN)
    cut_paper(x+newN, y, newN)
    cut_paper(x+newN, y+newN, newN)
  return

# N * N 색종이
# 0 : 하얀색 / 1 : 파란색
# 전체 색종이 입력받기
N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# white, blue 개수 초기화
white = 0
blue = 0

cut_paper(0, 0, N)
print(white)
print(blue)