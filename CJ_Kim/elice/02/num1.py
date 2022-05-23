
flatN, lazerH = map(int, input().split())
flatInfo = []
for _ in range(flatN):
    x, s, k = map(int, input().split())
    flatInfo.append([x, s, k])
def byX(array):
    return array[0]
flatInfo.sort(key=byX)

holeFlat = 0
finalX = -1

for flat in flatInfo:
    if flat[2]==3 and flat[1]>lazerH:
        finalX = flat[0]
        break
    if flat[2]==1 and flat[1]>lazerH:
        holeFlat += 1
print(finalX, holeFlat)
    
