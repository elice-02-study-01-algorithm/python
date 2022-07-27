
# 4번

def solution(beginning, target):
    def inverserow(row):
        arr = []
        for i in row:
            if i == 1:
                arr.append(0)
            else:
                arr.append(1)
        return arr

    row = len(target[0])
    col = len(target)
    answer = 0

    for i in range(col):
        if beginning[i] != target[i]:
            break

    for j in range(row):
        if beginning[i][j] != target[i][j]:
            answer += 1
            for k in range(col):
                beginning[k][j] = 1 if beginning[k][j] == 0 else 0
    
    for i in range(col):
        if inverserow(beginning[i]) == target[i]:
            answer += 1
        elif beginning[i] == target[i]:
            continue
        else:
            return -1

    return min(answer,len(target)+len(target[0])-answer)
