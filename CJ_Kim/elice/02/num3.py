dotN = int(input())
dotList = []

for _ in range(dotN):
    x, y = map(int, input().split())
    dotList.append([x, y])

# sort함수 쓰는 거 재밌당
dotList.sort(key=lambda x:x[0])

area = 0
for i in range(len(dotList)-1):
    x1, y1 = dotList[i]
    x2, y2 = dotList[i+1]
    # 평행사변형 공식
    area += ((y1+y2)*(x2-x1)*(1/2))

if area == int(area):
    print(int(area))
else:
    print(area)