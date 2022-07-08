# 운전할 거리의 최솟값 구하기
from sys import stdin
input = stdin.readline

shortcutCount, highwayLong = map(int, input().split())
shortcutInfo = []
for _ in range(shortcutCount):
    start, end, cost = map(int, input().split())
    # 고속도로 역주행 불가 -> '도착위치 > 고속도로 길이'면 쓸데없는 정보
    if end > highwayLong:
        continue
    # 지름길 효율: 도착위치 - 시작위치 - 지름길 길이 = 음수면 쓸데없는 정보
    if end - start - cost < 0:
        continue
    # node.update([start, end])
    shortcutInfo.append((start, end, cost))

fastest = [i for i in range(highwayLong + 1)]
for cur in range(highwayLong + 1):
    fastest[cur] = min(fastest[cur], fastest[cur-1] + 1)
    for s, e, c in shortcutInfo:
        if cur == s and fastest[cur] + c < fastest[e]:
            fastest[e] = fastest[cur] + c
# print(fastest)
print(fastest[highwayLong])