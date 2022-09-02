# 코드리뷰 안하셔도 됩니다!
# 혹시나 아이디어 힌트가 있다면 그것만이라도 짧게 남겨주시면 좋을 것 같습니다.
# 시간 초과+실패 6.3점
'''
def solution(n, lighthouse):
    answer = 0

    mainLightHouse = []

    lightHouseDict = {List1: [] for List1 in range(1, n+1)}
    
    for a, b in lighthouse:
        lightHouseDict[a].append(b)
        lightHouseDict[b].append(a)

    sortByLen = dict(sorted(lightHouseDict.items(), key=lambda item: len(item[1])))
    # print(sortByLen)

    def lightOn(lightMap, lightList):
        visited = []
        for i in lightList:
            visited+=lightMap[i]
            visited.append(i)
        return visited
    
    lightsOn = []
    allLightHouse = [i for i in range(1, n+1)]
    for house, adjacent in sortByLen.items():
        
        lightsOn += lightOn(lightHouseDict, adjacent)
        lightsOn = list(set(lightsOn))
        mainLightHouse+=adjacent
        mainLightHouse = list(set(mainLightHouse))
        if sorted(lightsOn) == allLightHouse:
            break
    answer = len(mainLightHouse)
    return answer
'''
# 미완성 코드입니다.
# 아이디어조차 생각나지 않아요!
def solution(n, lighthouse):
    lightsOnList = [i for i in range(1, n+1)]

    lightHouseDict = {List1: [] for List1 in range(1, n+1)}
    
    for a, b in lighthouse:
        lightHouseDict[a].append(b)
        lightHouseDict[b].append(a)
    
    sortByLen = dict(sorted(lightHouseDict.items(), key=lambda item: len(item[1])))
    # print(sortByLen)
    
    def oneSideBFS(lightHouseList):
        lightedOn = set()
        for lightHouse in lightHouseList:
            lightedOn.add(lightHouseDict[lightHouse])
            if list(lightedOn) == [i for i in range(1, n+1)]:
                return True
    
    for idx, adjacent in sortByLen.items():
        if len(adjacent) == 1:
            lightsOnList.remove(idx)
    
    

    while True:
        if oneSideBFS(lightsOnList):
            break
        
    
    print(lightsOnList)

    return len(lightsOnList)

    

    


print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))