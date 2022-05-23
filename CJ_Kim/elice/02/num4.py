dotN = int(input())
dotList = []
for _ in range(dotN):
    x, y = map(int, input().split())
    doNotAppend = False
    for dot in dotList:
        if dot[0] == x and dot[1]>=y:
            doNotAppend = True
            break
        elif dot[0] == x and dot[1]<y:
            dotList.remove([dot[0], dot[1]])
            dotList.append([x, y])
            break
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