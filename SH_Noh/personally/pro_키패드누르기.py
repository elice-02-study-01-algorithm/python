# 왼손 : 1, 4, 7 -> 3으로 나눴을 때 나머지 1
# 오른손 : 3, 6, 9 -> 3의 배수
# 나머지 : 마지막 위치에서 더 가까운 손
# 현재 왼손, 오른손 위치는 0이 원점인 좌표로 표기

def solution(numbers, hand):
    # numInfo = {1: (-1, 3), 2: (0, 3), 3: (1, 3), 4: (-1, 2), 5: (0, 2), 6: (1, 2), 7: (-1, 1), 8: (0, 1), 9:(1, 1), 0: (0, 0)}
    numInfo = {1: (0, 3), 2: (1, 3), 3: (2, 3), 4: (0, 2), 5: (1, 2), 6: (2, 2), 7: (0, 1), 8: (1, 1), 9:(2, 1), 0: (1, 0)}

    result = ["L"] * len(numbers)
    left = (-1, 0)
    right = (0, 1)
    for i, num in enumerate(numbers):
        if num % 3 == 0 and num != 0: # right
            right = numInfo[num]
            result[i] = "R"
        elif num % 3 == 1: # left
            left = numInfo[num]
        else: # 나머지
            tx, ty = numInfo[num]
            rx, ry = right
            lx, ly = left
            distanceR = abs(tx-rx) + abs(ty-ry) # 0-0 + 2-1
            distanceL = abs(tx-lx) + abs(ty-ly) # 0--1 + 2-3
            if distanceR < distanceL:
                right = numInfo[num]
                result[i] = "R"
            elif distanceR > distanceL:
                left = numInfo[num]
            else:
                if (hand == "right"):
                    right = numInfo[num]
                    result[i] = "R"
                else:
                    left = numInfo[num]
    
    return "".join(result)

print(solution([1, 5, 7, 9, 4, 6, 2, 5, 5], "left"))