'''
🍔
햄버거 포장
햄버거: 빵-야채-고기-빵
정해진 순서로 쌓인 햄버거만 포장
재료의 정보 나타내는 정수 배열 ingredient가 주어졌을 때,
포장하는 햄버거의 개수를 return
빵: 1, 야채: 2, 고기: 3
'''

'''
시간 초과 41.2점
'''
'''
def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    index = 0
    while index<len(ingredient):
        if ingredient[index:index+4] == hamburger:
            ingredient = ingredient[0:index] + ingredient[4:]
            answer += 1
            index -= 1
        index += 1
    
    return answer
'''
# 시간 초과 41.2
'''
def solution(ingredient):
    global answer
    answer = 0
    hamburger = [1, 2, 3, 1]
    index = 0
    def makeHamburger(ingreList, curIndex):
        global answer
        if len(ingreList)<4:
            return 
        for idx in range(curIndex, len(ingreList)):
            if ingreList[idx:idx+4] == hamburger:
                answer += 1
                return makeHamburger(ingreList[0:idx]+ingreList[idx+4:], idx-1)
        return
    makeHamburger(ingredient, index)
    
    return answer
'''
# 82.4점
def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    hamburgerStack = []
    for ingre in ingredient:
        # 전체 ingredient를 돌면서 재료 하나씩 stack에 넣기
        hamburgerStack.append(ingre)
        # 마지막 원소 4개가 햄버거일 때, 포장하기
        if len(hamburgerStack)>=4 and hamburgerStack[-4:] == hamburger:
            # 아마 pop()으로 했으면 100점을 맞지 않았을까...
            hamburgerStack = hamburgerStack[:-4]
            answer += 1
            
    return answer
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))