operator = input()
# - 인거 다 분리
minus_splitted = operator.split('-')
result_list = []
for m in minus_splitted:
    # + 인거 다 분리
    plus_splitted = m.split('+')
    accumulate = 0
    # + 인거 다 더해서 넣어줌
    for plus in plus_splitted:
        accumulate += int(plus)
    result_list.append(accumulate)
# 계산을 위해 첫번째꺼 꺼내고 나머지 다 빼준다
result = result_list[0]
for r in result_list[1:]:
    result -= r
print(result)