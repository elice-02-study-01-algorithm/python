# 매일 할인 품목 하나 구매
# 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치해야 함
# number(총 원하는 개수)의 합은 10
def solution(want, number, discount):
    answer = 0
    # needs = { name: value for name, value in zip(want, number) }
    for day in range(len(discount) - 9):
        start = day
        end = day + 10
        needs = { name: value for name, value in zip(want, number) }
        for i in range(start, end):
            today_product = discount[i]
            if today_product in needs:
                if needs[today_product] > 0:
                    needs[today_product] -= 1

        # 0만 있는지 확인
        result = set(needs.values())
        if len(result) == 1 and 0 in result:
            answer += 1

    return answer

# 100점