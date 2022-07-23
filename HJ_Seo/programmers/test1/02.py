# 2번.

def solution(want, number, discount):
    answer = 0
    x = []
    for i in range(len(number)):
        x += [want[i]]*number[i]

    want1 = sorted(x)
    total = sum(number)

    for i in range(len(discount)-total+1):
        if want1 == sorted(discount[i:i+total]):
            answer += 1

    return answer
