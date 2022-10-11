'''
T[N] = [wine[N]을 포함한 포도주 합, wine[N]을 포함하지 않은 포도주 합]
T[N] = [max(T[N-2][0] + wine[N],  T[N-2][1] + wine[N-1] +  wine[N]), max(T[N-1])]
[0, 6, 10, 13, 9, 8, 1]
'''
# readline 쓰기 전 = 476ms
# readline 쓴 후 = 84ms
# input이 10000 이하인데도 차이가 심하게 나네요!
import sys
input = sys.stdin.readline

wineGlassNum = int(input())
wineGlass = [0]

for _ in range(wineGlassNum):
    wineGlass.append(int(input()))

if wineGlassNum < 3:
    print(sum(wineGlass))
    exit()

wineMaxSum = [[0, 0]]+[[wineGlass[1], 0]]+[[wineGlass[1]+wineGlass[2], wineGlass[1]] ]+ [[0, 0] for _ in range(wineGlassNum-2)]

for i in range(3, wineGlassNum+1):
    # 맨 위의 점화식을 그대로 수식화했습니다.
    selfIncludeMax = max(wineMaxSum[i-2][0] + wineGlass[i], wineMaxSum[i-2][1]+wineGlass[i-1]+wineGlass[i])
    selfExcludeMax = max(wineMaxSum[i-1])

    wineMaxSum[i] = [selfIncludeMax, selfExcludeMax]

print(max(wineMaxSum[wineGlassNum]))
