import sys
from itertools import product
input = sys.stdin.readline

targetChannel = int(input())
brokenButtonNum = int(input())
pressBasic = len(str(targetChannel))
# 아래의 채널의 경우 100에서 +- 누르는 것보다 번호누르고 바로 이동하는 게 더 빨라요
exceptionChannel = [99, 100, 101, 102]

# 숫자 N을 NNN으로 만들고 싶을 때 makeRepeatNum(3, N)
def makeRepeatNum(num, repeat):
    return int(str(num)*repeat)

# 가능한 채널들 중 누르는 횟수에 따라 가장 낮은 수 반환
def getLowestNum(possibleChannel, pressNum):
    # ex. 
    # 99999
    # 8
    # 2 3 4 5 6 7 8 9
    # possibleChannel = [0, 1]
    # pressNum = 6
    # return : 100000
    if len(possibleChannel)==1:
        return makeRepeatNum(possibleChannel[0], pressNum)
    minFirst = possibleChannel[0] if possibleChannel[0] != 0 else possibleChannel[1]
    lowestNum = str(minFirst) + str(possibleChannel[0])*(pressNum-1)
    return int(lowestNum)

# 만약 모든 버튼 작동가능할 때
if brokenButtonNum==0:
    # 예외 채널 인 경우는 별도 처리
    if targetChannel in exceptionChannel:
        print(abs(targetChannel-100))
        exit()
    print(pressBasic)
    exit()
else:
    brokenButtonList = list(map(int, input().strip().split()))

# 정상작동하는 버튼 리스트
normalButton = [i for i in range(10) if i not in brokenButtonList]

# 정상작동하는 버튼 리스트로 누를 수 있는 채널 리스트
possibleChannelList = []

# 중복순열
for channelTupple in product(normalButton, repeat=pressBasic):
    # ex. normalButton = [5, 6, 7, 8, 9]일 경우
    # (5, 5, 5), (5, 5, 6), (5, 5, 7) , ..., (9, 9, 8), (9, 9, 9)
    possibleChannel = ''
    for num in channelTupple:
        # (5, 5, 5) -> '555'
        possibleChannel+=str(num)
    possibleChannelList.append(int(possibleChannel))

# target을 기준으로 더 수가 낮은 채널과 높은 채널 분리 
lowerChannelList = []
higherChannelList = []

for channel in possibleChannelList:
    if channel < targetChannel:
        lowerChannelList.append(channel)
    # 만약 누를 수 있는 리스트 안에 가고 싶은 채널이 바로 있는 경우
    elif channel == targetChannel:
        if channel in exceptionChannel:
            print(abs(targetChannel-100))
            exit()
        print(pressBasic)
        exit()
    else:
        higherChannelList.append(channel)

compareList = []


if lowerChannelList==[]:
    # 모든 버튼이 고장나서 누를 수 있는 버튼이 없는 경우
    if higherChannelList==[]:
        print(abs(targetChannel-100))
        exit()
    # 가고 싶은 채널이 일의 자리 수가 아닌 경우
    # ex. 
    # 433
    # 8
    # 1 2 3 4 5 6 7 8
    # 99를 넣기 999-433 = 566 / 433-99 = 434
    if pressBasic!=1:
        compareList.append(makeRepeatNum(possibleChannel[-1], (pressBasic-1)))
    # 가고 싶은 채널에 가장 가까운 채널 넣기
    compareList.append(higherChannelList[0])
else:
    compareList.append(lowerChannelList[-1])
    # 가고 싶은 채널보다 작은 것들만 있을 때 
    if higherChannelList==[]:      
        compareList.append(getLowestNum(normalButton, pressBasic+1))
    else:
        compareList.append(higherChannelList[0])

# 버튼을 누르는 채널
pressChannel = 0
# 최소 차이
minDiff = float("inf")
for channel in compareList:
    # abs(targetChannel-channel)은 곧 +, -를 누르는 횟수를 의미
    if abs(targetChannel-channel) < minDiff:
        minDiff = abs(targetChannel-channel)
        pressChannel = channel

answer = min(len(str(pressChannel)) + abs(targetChannel-pressChannel), abs(targetChannel-100))
print(answer)

'''
애먹었던 반례 리스트
1555
3
0 1 9
670
671

99999
8
2 3 4 5 6 7 8 9
7

0
1
0
'''