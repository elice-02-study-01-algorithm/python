# 2000.01.00부터 몇 일이 지났는지 계산
def from2000(year, month, day):
    return (int(year)-2000)*12*28+(int(month)*28)+int(day)

def solution(today, terms, privacies):
    answer = []
    termInfo = {}

    todayYear, todayMonth, todayDay = today.split(".")
    # 오늘의 일 수
    todayDaysFrom2000 = from2000(todayYear, todayMonth, todayDay)

    # 각 유효기간 별 일 수
    for term in terms:
        termType, termDuration = term.split()
        termInfo[termType] = termDuration

    # 날짜와 약관에 따른 유효기간의 차이를 구합니다
    for i in range(len(privacies)):
        date, termType = privacies[i].split()
        limitMonth = termInfo[termType]
        limitDays = int(limitMonth)*28
        year, month, day = date.split(".")

        diffDay = todayDaysFrom2000-from2000(year, month, day)
        # 약관보다 오늘날이 더 많은 경우 파기해야하는 answer에 담기
        if limitDays <= diffDay:
            answer.append(i+1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))