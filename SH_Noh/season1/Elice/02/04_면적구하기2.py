# 같은 x값을 가질 수 있는 N개의 점
# 엘리스 토끼는 모든 점의 위치에 못을 박았음
# 실로 모든 점을 연결하고 끝은 늘어뜨렸을 때 그 안의 면적은?
# 만약 같은 x축에 둘 이상의 못이 박힌 경우 가장 높은 못에 묶음

from sys import stdin
inputs = stdin.readline

dotCount = int(inputs())
dotInfo = [tuple(map(int, input().split())) for _ in range(dotCount)]
dotInfo.sort(key = lambda x: (x[0], -x[1]))
# print(dotInfo)

area = 0
cx, cy = dotInfo[0]
for i in range(1, len(dotInfo)):
    nx, ny = dotInfo[i]
    if cx == nx:
        continue
    # print(cx, cy)
    # print(nx, ny)
    area += (cy + ny) * (nx - cx) / 2
    cx, cy = nx, ny

if area % 1 == 0:
    print(int(area))
else:
    print(area)
