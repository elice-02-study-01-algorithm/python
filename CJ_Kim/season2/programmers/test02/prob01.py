'''
학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때,
학생들 중 삼총사를 만들 수 있는 방법의 수를 return
삼총사: 번호의 합이 0
'''
from itertools import combinations

def solution(number):
    threeMusketeers = 0

    for i in combinations(number, 3):
        if sum(i) == 0:
            threeMusketeers += 1

    return threeMusketeers

solution([-2, 3, 0, 2, -5]) # 2
solution([-3, -2, -1, 0, 1, 2, 3]) # 5
solution([-1, 1, -1, 1]) # 0