dotN = int(input())
dotList = []

# 앞의 문제와 거의 유사한 줄 알았으나 데이터 구축 때
# 조금 진을 뺐음
for _ in range(dotN):
    x, y = map(int, input().split())
    # 이중 for 문 처리 위한 변수
    doNotAppend = False
    for dot in dotList:
        # 들어오는 좌표의 x값이 이미 존재하고,
        # 넓이를 구하는 데에 영향을 주지 않는 것일 때
        # == y 값이 이미 들어간 것보다 작을 때
        if dot[0] == x and dot[1]>=y:
            doNotAppend = True
            break
        # 들어오는 좌표의 x값이 이미 존재하고,
        # 들어있는 것보다 y값이 클 때 갈아치우기
        elif dot[0] == x and dot[1]<y:
            dotList.remove([dot[0], dot[1]])
            dotList.append([x, y])
            break
    # 새로운 좌표일 때
    if [x, y] not in dotList and doNotAppend==False:
        dotList.append([x, y])

dotList.sort(key=lambda x:x[0])

area = 0
for i in range(len(dotList)-1):
    x1, y1 = dotList[i]
    x2, y2 = dotList[i+1]
    area += ((y1+y2)*(x2-x1)*(1/2))
    
if area == int(area):
    print(int(area))
else:
    print(area)