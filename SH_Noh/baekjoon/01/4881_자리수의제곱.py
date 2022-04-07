import sys

cases = []
while True: # 0 0이 입력될 때까지 입력받기
    case = list(sys.stdin.readline().strip().split())
    if case == ['0', '0']:
        break
    cases.append(case)

def sumEach(case):
    sequence1 = [int(case[0])]
    sequence2 = [int(case[1])]
    isEnd1 = False
    isEnd2 = False
    while (not isEnd1 or not isEnd2):
        if sequence1 == sequence2:
            return 2

        sum1 = 0
        sum2 = 0
        for i in str(sequence1[-1]): # 각 자리수의 제곱의 합 구하기
            sum1 += int(i) ** 2
        if sum1 in sequence1: # 자리수의 제곱의 합이 list에 이미 있으면
            isEnd1 = True # list 조합 완성
        else:
            sequence1.append(sum1) # 없으면 list에 추가

        for i in str(sequence2[-1]):
            sum2 += int(i) ** 2
        if sum2 in sequence2:
            isEnd2 = True
        else:
            sequence2.append(sum2)

    if set(sequence1) & set(sequence2): # 만약 겹치는 수(교집합)가 있으면
        common1 = [x for i in sequence1 for x in sequence2 if i == x][0] # sequence1를 기준으로 처음으로 겹치는 수
        common2 = [x for i in sequence2 for x in sequence1 if i == x][0] # sequence2를 기준으로 처음으로 겹치는 수
        result1 = sequence1.index(common1) + sequence2.index(common1) + 2 # common1 기준 길이의 합
        result2 = sequence1.index(common2) + sequence2.index(common2) + 2 # common2 기준 길이의 합
        return min(result1, result2) # 두 수열 길이의 합의 최솟값 return
    else: # 만약 겹치는 수(교집합)가 없으면
        return 0

for case in cases: # 각각의 경우에 대해 계산하고 출력
    result = sumEach(case)
    print(f'{case[0]} {case[1]} {result}')
