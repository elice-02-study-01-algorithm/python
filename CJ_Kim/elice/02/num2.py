# 문제가 너무 길어서 어려울 줄 알았으나 그냥 냅다 길기만 했던 거임
# 입력 순서가 일반적이지 않아서 테스트하기가 너무 불편했음
numN, playerN, answer, roundN = map(int, input().split())

callList = []
for _ in range(playerN):
    callList.append(list(map(int, input().split())))

startP = 0
numList = [i for i in range(1, numN+1)]

finishRound = 0
finishPlayer = 0
# 이중 for문 탈출위한 변수
breaktwice = False

for i in range(roundN):
    for j in range(playerN):
        # out of index 오류 방지 위한 인덱스 조정
        if startP < 0:
            startP = numN+startP
        startP -= callList[j][i]%numN
        currentN = numList[startP]
        # 플레이어가 정답을 맞춘 경우
        if currentN == answer:
            finishRound = i+1
            finishPlayer = j+1
            breaktwice = True
            break
    if breaktwice == True:
        break
if finishRound == 0 and finishPlayer == 0:
    print(-1)
else:
    print(finishPlayer, finishRound)