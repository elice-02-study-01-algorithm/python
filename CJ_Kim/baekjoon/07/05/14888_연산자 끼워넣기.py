import sys
from itertools import permutations
input = sys.stdin.readline

num = int(input())
seq = list(map(int, input().strip().split()))
ops = list(map(int, input().strip().split()))


opsNumList = []
for idx, val in enumerate(ops):
    for _ in range(val):
        opsNumList.append(idx)

opsPerList = []
for i in permutations(opsNumList, len(opsNumList)):
    opsPerList.append(i)

maxNum = float("-inf")
minNum = float("inf")

def doCal(number1, operator, number2):
    print(number1, operator, number2)
    if operator == 0:
        return number1 + number2
    elif operator == 1:
        return number1 - number2
    elif operator == 2:
        return number1 * number2
    else:
        if number1 < 0:
            return -(-(number1)//number2)
        else:
            return number1//number2

# result = seq[0]
# for eachNum in seq[1:]:
#     for opList in opsPerList:
#         for op in opList:
#             result = doCal(result, op, eachNum)
#             print('result', result, maxNum, minNum)
#             if result > maxNum:
#                 maxNum = result
#             if result < minNum:
#                 minNum = result

numList = [seq for _ in range(len(opsPerList))] 
for i in range(len(opsPerList)):
    opList = opsPerList[i]
    eachNumList = numList[i]
    result = eachNumList[0]
    for eachNum in eachNumList[1:]: 
        for op in opList:
            result = doCal(result, op, eachNum)
            print('result', result, maxNum, minNum)
    if result > maxNum:
        maxNum = result
    if result < minNum:
        minNum = result
    
print(maxNum, minNum)