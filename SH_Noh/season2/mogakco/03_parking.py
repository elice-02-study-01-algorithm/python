# 차량번호 별 머무른 시간 구하기
# fees에 의거하여 요금 구하기
# 차량번호가 작은 순으로 return
import datetime
import math
def solution(fees, records):
    answer = []
    car_in_record = {}
    car_stay_time = {}
    remains = []
    
    # 자동차별 머문 시간 계산
    for record in records:
        time, car, status = record.split()
        time = datetime.datetime.strptime(time, "%H:%M")
        if status == "IN":
            car_in_record[car] = time
            remains.append(car)
        else:
            stay = time - car_in_record[car]
            if car not in car_stay_time:
                car_stay_time[car] = stay
            else:
                car_stay_time[car] += stay
            remains.remove(car)
            
    # OUT 없이 남아있는 차들 처리
    for car in remains:
        stay = datetime.datetime.strptime("23:59", "%H:%M") - car_in_record[car]
        if car not in car_stay_time:
                car_stay_time[car] = stay
        else:
            car_stay_time[car] += stay
            
    # 주차 요금 계산
    charge = []
    cars = sorted(list(car_stay_time.keys()))
    for car in cars:
        stay = car_stay_time[car]
        total_minutes = divmod(stay.seconds, 60)[0]
        # 기본 시간 이하라면
        if total_minutes <= fees[0]:
            charge.append(fees[1])
        # 기본 시간 초과하면
        else:
            exceed = fees[1] + math.ceil(((total_minutes - fees[0])/fees[2])) * fees[3]
            charge.append(exceed)
    
    return charge