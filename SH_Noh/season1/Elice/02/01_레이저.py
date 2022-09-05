# 판자 너비는 항상 1m, 높이는 다양함, 겹치지 않음
# 판자의 재질은 나무, 고무, 강철
# 레이저는 항상 x = 0, y = height 위치에서 쏨'
# 레이저 높이 == 나무판자 높이 : 판자를 만나지 않은 것
# 판자 == 나무(1) : 구멍, 통과
# 판자 == 고무(2) : 멀쩡, 통과
# 판자 == 강철(3) : 멀쩡, 멈춤
# 레이저가 멈추는 지점의 x좌표, 구멍이 뚫리는 판자의 개수 출력
# 레이저가 멈추지 않는다면 x좌표는 -1 출력

from sys import stdin
inputs = stdin.readline

boardCount, height = map(int, inputs().split())
boardInfo = [tuple(map(int, input().split())) for _ in range(boardCount)]
boardInfo.sort(key = lambda x: x[0])

stop = -1 # 값이 변하지 않으면 레이저 끝까지 강철이 없었던 것(멈추지 않은 것)
hole = 0

for board in boardInfo:
    # 판자의 왼쪽 아래 꼭짓점, 판자의 세로 길이, 판자의 성질
    x, h, m = board
    if m == 3 and h > height: # 강철이면 멈춤
        stop = x
        break
    if m == 1 and h > height: # 나무면 구멍
        hole += 1

print(stop, hole)