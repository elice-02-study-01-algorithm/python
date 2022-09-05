# http://daplus.net/python-float-%EA%B0%92%EC%9D%B4-%EC%A0%95%EC%88%98%EC%9D%B8%EC%A7%80-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95/
# 같은 x값을 가지지 않는 N개의 점
# 엘리스 토끼는 모든 점의 위치에 못을 박았음
# 실로 모든 점을 연결하고 끝은 늘어뜨렸을 때 그 안의 면적은?
# 면적이 정수면 정수, 실수면 실수 그대로 출력

# 같은 x값을 가지지 않는 N개의 점
# 엘리스 토끼는 모든 점의 위치에 못을 박았음
# 실로 모든 점을 연결하고 끝은 늘어뜨렸을 때 그 안의 면적은?
# 면적이 정수면 정수, 실수면 실수 그대로 출력

from sys import stdin
inputs = stdin.readline

dotCount = int(inputs())
dotInfo = [tuple(map(int, input().split())) for _ in range(dotCount)]
dotInfo.sort(key = lambda x: x[0])

area = 0
for i in range(len(dotInfo) - 1):
    cx, cy = dotInfo[i]
    nx, ny = dotInfo[i+1]
    area += (cy + ny) * (nx - cx) / 2

if area % 1 == 0:
    print(int(area))
else:
    print(area)
