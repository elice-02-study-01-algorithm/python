# 2022년 7월 31일 모각코.
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def change_time(arr):
    t,m = arr.split(':')
    return int(t)*60+int(m)

def solution(fees, records):
    #fee : 0 == 기본시간, 1 == 기본요금, 2 == 단위시간당, 3 == 요금.
    def change_time_to_fee(time):
        cal_time = (max(0,(time-fees[0])/fees[2]))
        if int(cal_time) != cal_time:
            cal_time = int(cal_time)+1
        # print(cal_time)
        return fees[1]+cal_time*fees[3]
    
    last_time = change_time('23:59')
    in_time = dict()
    result_time = dict()
    
    for record in records:
        time,num,in_out = record.split()
        time = change_time(time)
        
        if in_out == 'IN':
            in_time[num] = time
        elif in_out == 'OUT':
            if num not in result_time:
                result_time[num] = 0
            result_time[num] += time-in_time[num]
            del in_time[num]
        
    for num in in_time:
        if num not in result_time:
            result_time[num] = 0
        result_time[num] += last_time - in_time[num]
    
    # print(result_time)
    num_lst = sorted(result_time.keys())
    # print(num_lst)
    time_sort = [result_time[num] for num in num_lst]
    
    # print(time_sort)
    answer = [change_time_to_fee(time) for time in time_sort]
    
    return answer