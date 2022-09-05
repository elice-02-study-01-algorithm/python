import math
def solution(fees, records):

    basicT, basicF, unitM, unitF = fees
    parkingInfo = {}

    # parkingInfo
    # {'5961': ['05:34', '07:59', '22:59', '23:00'], '0000': ['06:00', '06:34', '18:59'], '0148': ['07:59', '19:09']}
    for record in records:
        time, number, _ = record.split()
        try:
            parkingInfo[str(number)].append(time)
        except:
            parkingInfo[str(number)] = []
            parkingInfo[str(number)].append(time)

    # 16:30 의 형태를 자정으로부터의 분으로 환산(구간을 구하기에 용이)
    def toMinute(timeStr):
        hour, minute = timeStr.split(":")
        result = int(hour)*60 + int(minute)
        return result

    # 요금 계산하기
    def calculateFee(timeList):
        totalTime = 0
        for timeIdx in range(0, len(timeList), 2):
            # 얼마동안 있었는지 계산
            totalTime += toMinute(timeList[timeIdx+1]) - toMinute(timeList[timeIdx])

        # 기본 시간 이하일 경우 기본 요금
        if totalTime<=basicT:
            return basicF
        else:
            leftTime = totalTime - basicT
            # 단위 시간으로 나눈 것 올림해서 계산
            return basicF + math.ceil(leftTime/unitM)*unitF

    # 금일 나간 기록이 없으면 채워주기
    # 들어오고 나가는 거는 항상 쌍을 이루므로, 기록이 짝수가 아니면 나간 게 아님
    for val in parkingInfo.values():
        if len(val) %2 != 0:
            val.append('23:59')
    
    # 자동차 넘버와 주차 요금을 같이 담은 리스트
    carAndFeeList = []
    for carNumber, parkingTimeList in parkingInfo.items():
        carAndFeeList.append([carNumber,calculateFee(parkingTimeList)])

    # 자동차 넘버 순으로 정렬하기
    carAndFeeList.sort()

    answer = []

    # 주차 요금만 담은 리스트
    for i in carAndFeeList:
        answer.append(i[1])

    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])
