def solution(ingredient):
    answer = 0
    gar = []
    for i in ingredient:
        gar.append(i)
        if gar[-4:] == [1,2,3,1]:
            gar.pop()
            gar.pop()
            gar.pop()
            gar.pop()
            answer+=1

    return answer