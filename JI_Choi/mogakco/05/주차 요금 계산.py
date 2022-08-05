import math

def solution(fees, records):
    # 딕셔너리 선언
    dict = {}
    # 키 값 배열 선언
    keys = []

    # 입력값을 딕셔너리 형태로 변환
    for info in records:
        carNum = info[6:10]
        # 차번호가 키 값으로 이미 존재하는 경우
        if carNum in dict:
            # 시간 정보 추가
            dict[carNum] += [info[0:5]]
        # 존재하지 않는 경우
        else:
            # 새로운 딕셔너리 생성
            dict[carNum] = [info[0:5]]
            # 키 값 배열에 차번호 추가
            keys.append(carNum)

    # 키 값 내림차순 정렬
    keys.sort()

    # 자동차별 주차 요금을 담을 배열 선언
    answer = []

    # 차번호가 작은 순서로 순회
    for key in keys:
        time = 0
        # 시간 정보의 길이 확인
        d = len(dict[key])
        # 출차 기록이 없는 경우 (시간 정보의 길이가 홀수인 경우)
        if d % 2 == 1:
            # 출차 기록 추가
            dict[key] += ['23:59']

        # 시간(단위: 분) 계산
        for i in range(0, d, 2):
            time += 60*(int(dict[key][i+1][0:2]) - int(dict[key][i][0:2])) + int(dict[key][i+1][3:5]) - int(dict[key][i][3:5])

        # 기본 시간보다 짧은 경우
        if time < fees[0]:
            answer.append(fees[1])
        # 기본 시간보다 긴 경우
        else:
            calculated_fee = fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3]
            answer.append(calculated_fee)

    # 자동차별 주차 요금 반환
    return answer

# 테스트 값
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))