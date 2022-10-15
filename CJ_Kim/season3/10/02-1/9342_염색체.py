# 신박한 풀이 👀
#https://www.acmicpc.net/source/49490214

import sys
import re
from string import ascii_uppercase

input = sys.stdin.readline
# 염색체에 들어가는 문자들
choromoBasic = ['A', 'B', 'C', 'D', 'E', 'F']

caseNumber = int(input())

for _ in range(caseNumber):
    answer = 'Good'

    choromo = input()
    choromoList = list(choromo)

    pattern = re.compile('[A-F]?A+F+C+[A-F]?')
    # [전체 대분자 알파벳]-[염색체에 들어가는 알파벳]
    notChoromo = [x for x in ascii_uppercase if x not in choromoBasic]
    
    # 정규식에 통과하지 못하면 Good으로 출력됩니다
    if pattern.match(choromo)!=None:
        # 여기 들어오면 정규식에 통과되는데, 마지막 조건 중 
        
        passedLast = 'undefined'

        for piece in choromoList:
            if piece in notChoromo:
                passedLast = 'false'
                break

        if passedLast != 'false':
            answer = "Infected!"

    print(answer)