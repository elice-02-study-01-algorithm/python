from math import ceil

def changeTime(time):
    return 60 * (int(time[0:2])) + int(time[3:5])

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]

    car_dict = {}
    check_car_in_dict = {}

    for i in range(len(records)):
        time, car_number, state = records[i].split(' ')
        print(state)
        if state == "OUT":
            input_t = car_dict[car_number]
            output_t = changeTime(time)
            result_t = output_t - input_t
            check_car_in_dict[car_number][0] += (result_t)
            check_car_in_dict[car_number][1] ="OUT"
        else:
            car_dict[car_number] = changeTime(time)
            # 이미 입차 이력이 있는 차라면
            if car_number in check_car_in_dict:
                check_car_in_dict[car_number][1] = "IN"
            # 처음 입차하는 차라면
            else:
                check_car_in_dict[car_number] = [0, "IN"]

    check_car_in_dict = sorted(check_car_in_dict.items())
    for info in check_car_in_dict:
        number , result_time = info
        if result_time[1] == 'IN':
          result_time[0] += changeTime("23:59") - car_dict[number]
        if result_time[0] <= default_time:
            answer.append(default_fee)
        else:
            answer.append(default_fee + ceil(
                (result_time[0] - default_time) / unit_time) * unit_fee)        
        
    return answer