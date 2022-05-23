numN, playerN, answer, roundN = map(int, input().split())

callList = []
for _ in range(playerN):
    callList.append(list(map(int, input().split())))

startP = 0
numList = [i for i in range(1, numN+1)]

finishRound = 0
finishPlayer = 0
breaktwice = False
for i in range(roundN):
    for j in range(playerN):
        if startP < 0:
            startP = numN+startP
        startP -= callList[j][i]%numN
        
        currentN = numList[startP]
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