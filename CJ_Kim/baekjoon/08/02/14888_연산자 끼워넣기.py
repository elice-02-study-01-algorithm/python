import sys
input = sys.stdin.readline

num = int(input())
seq = list(map(int, input().strip().split()))
ops = list(map(int, input().strip().split()))

# 최댓값과 최솟값을 각각 음의 무한대와 양의 무한대로 초기화
maxNum = float("-inf")
minNum = float("inf")

# 사칙연산 결과값 반환 0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈
def doCal(number1, operator, number2):
    if operator == 0:
        return number1 + number2
    elif operator == 1:
        return number1 - number2
    elif operator == 2:
        return number1 * number2
    else:
        return int(number1/number2)

# 재귀 및 백트래킹으로 연산 시도하기
def recursionCal(index, result, plus, minus, multi, division):
    global maxNum, minNum

    # 마지막 수까지 연산을 하면 최댓값, 최솟값 검사하여 갱신하기
    if index == num:
        maxNum = max(result, maxNum)
        minNum = min(result, minNum)
        return

    else:
        if plus>0:
            plus -= 1
            recursionCal(index+1, doCal(result, 0, seq[index]), plus, minus, multi, division)
            plus += 1
        
        if minus>0:
            minus -= 1
            recursionCal(index+1, doCal(result, 1, seq[index]), plus, minus, multi, division)
            minus += 1

        if multi>0:
            multi -= 1
            recursionCal(index+1, doCal(result, 2, seq[index]), plus, minus, multi, division)
            multi += 1

        if division>0:
            division -= 1
            recursionCal(index+1, doCal(result, 3, seq[index]), plus, minus, multi, division)
            division += 1
        
recursionCal(1, seq[0], ops[0], ops[1], ops[2], ops[3])
print(maxNum)
print(minNum)