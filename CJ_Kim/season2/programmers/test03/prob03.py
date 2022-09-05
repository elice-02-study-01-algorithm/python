'''
💂‍♀️
보행은 1m/s의 일정한 속도로 나아간다.
감시하는 경비병의 구간은 서로 겹치지 않고, 근무-휴식을 일정 시간을 주기로 반복
근무 중에 지나가면 발각, 휴식 중에는 지나갈 수 있음
경비병의 근무 정보를 모르고 쉬지 않고 전진,

현재 위치와 적군 기지 사이의 거리를 나타내는 정수 distance
각 경비병의 감시 구간을 담은 2차원 정수 배열 scope,
같은 순서로 각 경비병의 근무 시간과 휴식 시간을 담은 2차원 정수 배열 times가 주어질 때,
경비를 피해 최대로 이동할 수 있는 거리를 return
'''

# 시간 초과 35.7점
'''
def solution(distance, scope, times):
    answer = 0
    isWorking = []
    for i in range(len(scope)):
        work, rest = times[i]
        tempRotate = []
        for _ in range(work):
            tempRotate.append(True)
        for _ in range(rest):
            tempRotate.append(False)
        tempRotate = tempRotate*((distance//(work+rest))+1)
        a, b = sorted(scope[i])
        for j in range(0, a-1):
            tempRotate[j] = 0
        for j in range(b, distance):
            tempRotate[j] = 0
        isWorking.append(tempRotate)
    isWorkingSlice = map(lambda x:x[:distance], isWorking)
    movingDistance = distance
    for soldier in isWorkingSlice:
        try:
            index = soldier.index(True) + 1
        except:
            index = distance
        movingDistance = min(movingDistance, index)
    answer = movingDistance
    return answer
'''

# 21.4점
'''
def solution(distance, scope, times):
    answer = 0
    isWorking = []
    for i in range(len(scope)):
        work, rest = times[i]
        a, b = sorted(scope[i])
        tempRotate = []
        for _ in range(work):
            tempRotate.append(True)
        for _ in range(rest):
            tempRotate.append(False)
        tempRotate = tempRotate*((distance//(work+rest))+1)
        for idx in range(len(tempRotate)):
            if idx < a-1 or b-1 < idx:
                tempRotate[idx] = 0
        print(tempRotate[:distance])
        isWorking.append(tempRotate[:distance])
    movingDistance = distance
    print(isWorking)
    for soldier in isWorking:
        try:
            index = soldier.index(True) + 1
        except:
            index = distance
        movingDistance = min(movingDistance, index)
    answer = movingDistance
    return answer

'''
# 64.3점 실패
'''
def solution(distance, scope, times):
    answer = distance
    for i in range(len(scope)):
        rangeA, rangeB = sorted(scope[i])
        work, rest = times[i]
        for j in range(rangeA, rangeB+1):
            if 0<j % ( work + rest) < work:
                answer = min(j, answer)

    return answer
'''
# 100점! 우앙!!
# ⭐️각 위치구간은 곧 화랑이의 시간대와 동일하다⭐️
def solution(distance, scope, times):
    # 한 번도 안 걸릴 경우
    answer = distance
    for i in range(len(scope)):
        # 각 경비병의 위치구간과 근무&휴식 주기를 추출
        rangeA, rangeB = sorted(scope[i])
        work, rest = times[i]
        # 각 위치 구간(==시간대)에서 근무/휴식하고 있는지 확인한다
        for j in range(rangeA, rangeB+1):
            # 화랑이가 지나갈 시점에 근무하고 있을 때 갱신하기
            if 0<j % ( work + rest) <= work:
                answer = min(j, answer)
            '''
            예시 1의 경우)
               X X 💂‍♀️ 💂‍♀️ 👮 👮 👮 👮 X X 
            💂‍♀️ W W  R  R  R  R R  W W R
            👮 W W  W  W  R  R R 'W' W W
                              (여기서 갱신)  
            '''

    return answer

print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]))
print(solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]]))