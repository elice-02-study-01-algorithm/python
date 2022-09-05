def solution(ingredient):
    answer = 0
    burger = []
    for ele in ingredient:
        burger.append(ele)
        if burger[-4:] == [1, 2, 3, 1]:            
            answer += 1
            for _ in range(4):
                burger.pop()
    return answer