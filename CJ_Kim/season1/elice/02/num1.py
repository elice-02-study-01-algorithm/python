
flatN, lazerH = map(int, input().split())
flatInfo = []

for _ in range(flatN):
    x, s, k = map(int, input().split())
    flatInfo.append([x, s, k])

# 레이저 맞는 순서대로 x값이 작은 것부터 나열
def byX(array):
    return array[0]
flatInfo.sort(key=byX)
'''
flatInfo.sort(key=lambda x:x[0])
'''

# 구멍이 나는 판대기 수
holeFlat = 0
# 멈추는 x 값
finalX = -1

# x축 방향으로 레이저 쏘기
for flat in flatInfo:
    # 강철이고 레이저 높이보다 높으면 STOP
    if flat[2]==3 and flat[1]>lazerH:
        finalX = flat[0]
        break
    # 나무이고 레이저 높이보다 높으면 구멍!
    if flat[2]==1 and flat[1]>lazerH:
        holeFlat += 1
        
print(finalX, holeFlat)
    
