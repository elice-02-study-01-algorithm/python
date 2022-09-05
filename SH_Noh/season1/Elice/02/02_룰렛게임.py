# https://rfriend.tistory.com/289
'''
from sys import stdin
import numpy as np
inputs = stdin.readline

numCount, playerCount, target, rounds = map(int, inputs().split())
gameInfo = [tuple(map(int, inputs().split())) for _ in range(playerCount)]
gameInfo = np.array(gameInfo)
gameInfo.T
print(gameInfo)

winner = -1
winRound = 0
'''
        
# 룰렛을 돌리면 선물을 가져갈 수 있음
# 사회자 1명, 플레이어 K명
# 1부터 N까지 시계방향으로 오름차순인 원판이 돌아감
# 사회자가 숫자 P를 결정, 플레이어는 순서대로 원판을 회전
# 원판의 화살표는 처음에 1을 가리킴
# 원판의 화살표 == P : 게임 종료, 해당 플레이어 승리
# 게임은 총 L라운드, 플레이어 1번부터 시작
# 플레이어가 원하는 만큼(N보다 클 수 있음) 시계방향으로 회전
# 최종 승리 플레이어 번호, 몇 번째 라운드에서 이겼는지 출력
# 만약 아무도 P를 맞히지 못하면 -1 출력

from sys import stdin
inputs = stdin.readline

numCount, playerCount, target, rounds = map(int, inputs().split())
gameInfo = [tuple(map(int, inputs().split())) for _ in range(playerCount)]
# print(gameInfo)
winner = 0
winRound = 0
roulette = 1

# 룰렛 : 1, 2, 3, 4, 5, 6
# 3명이 플레이
# P == 3
# 4라운드 진행
for i in range(rounds):
    for j, player in enumerate(gameInfo):
        move = player[i]
        roulette = (roulette - move) % numCount # 6은 0이 됨
        roulette = numCount if roulette == 0 else roulette
        # print(roulette)
        if roulette == target:
            winner = j + 1
            winRound = i + 1
            print(winner, winRound)
            exit()

print(-1)