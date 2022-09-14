from itertools import combinations

def solution(number):
    answer = 0
    result = list(combinations(number, 3))
    for r in result:
        if sum(r) == 0:
            answer += 1

    return answer