from itertools import combinations

def solution(number):
    cnt = 0
    for i in combinations(number,3):
        if sum(i) == 0:
            cnt += 1
    return cnt