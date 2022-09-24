def calculate(y, m, d, save):
    saveY = y
    saveM = m + save
    if saveM > 12:
        saveY += saveM // 12
        saveM %= 12
        if saveM == 0:
            saveM = 12
            saveY -= 1
    saveD = d - 1
    if saveD == 0:
        saveD = 28
        saveM -= 1
        if saveM == 0:
            saveM = 12
            saveY -= 1
    return saveY, saveM, saveD

def validate(today, saveY, saveM, saveD):
    year, month, day = map(int, today.split("."))
    if year < saveY:
        return True
    elif year == saveY:
        if month < saveM:
            return True
        elif month == saveM:
            if day <= saveD:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def solution(today, terms, privacies):
    answer = []
    # 유효기간의 단위는 달이고 100달까지 가능
    type_dict = {x.split()[0]: int(x.split()[1]) for x in terms}
    for i, v in enumerate(privacies):
        date, types = v.split(" ")
        y, m, d = map(int, date.split("."))
        # 유효기간 계산
        saveY, saveM, saveD = calculate(y, m, d, type_dict[types])
        # 넘는지 확인
        result = validate(today, saveY, saveM, saveD)
        if result == False:
            answer.append(i + 1)
    return answer