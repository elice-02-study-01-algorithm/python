# https://www.acmicpc.net/problem/1541
'''
아이디어
전체 연산 중에 -가 있기만 하면 이후의 것들을 양수건 음수건 모조리 음수 처리 해버립니다.
ex.
15 + 10 + 34 -> 그대로 연산
15 - 10 + 34 -> 15 - ( 10 + 34 ) == 15 - 10 - 34
15 - 10 - 34 -> 그대로 연산
'''

inputExpress = input()

minValue = 0
# - 뒤에 오는 것들을 담아놓은 리스트
minusNumStack = []
minusExist = False
tempNumber = ''
for pointer in inputExpress:
    # 연산이 아닐 경우 == 숫자일 경우
    if pointer != '-' and pointer != '+':
        tempNumber += pointer
    # 연산일 경우 앞의 숫자를 어떻게 처리할 것인지
    
    # -가 이미 나온 경우 저장한 숫자 -리스트로 보내버리기
    elif minusExist:
        minusNumStack.append(int(tempNumber))
        tempNumber = ''
    # -가 안 나왔는데, 방금 -가 나온 경우
    # boolean 바꾸고, 이전 것은 + 처리 해버리기
    elif pointer == '-':
        minValue += int(tempNumber)
        minusExist = True
        tempNumber = ''
    # -가 안 나오고 방금 +가 나온 경우
    # boolean 바꾸지 않고 + 처리 해버리기
    else:
        minValue += int(tempNumber)
        tempNumber = ''
        
# 다 돌고 나서 마지막 숫자 더하거나 뺴기       
if tempNumber:
    if minusExist:
        minusNumStack.append(int(tempNumber))
    else:
        minValue += int(tempNumber)

minValue -= sum(minusNumStack)

print(minValue)        
