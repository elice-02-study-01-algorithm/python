# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees
    
    dic = dict()

    for r in records:
        time, num, state = r.split(" ")
        num = int(num)
        
        if num in dic:
            dic[num].append([dateToMinutes(time), state])
        else:
            dic[num] = [[dateToMinutes(time), state]]
            
    rList = list(dic.items())
    rList.sort(key=lambda x : x[0])
    
    for r in rList:
        t = 0

        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == "IN":
            t += dateToMinutes('23:59')
        
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt) / ut) * uf)        

    return answer