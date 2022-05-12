# 코드리뷰하시는 분께서는 시간 초과난 코드 1과 맨 마지막 코드만 보시면 될 것 같습니다.
# 시간 초과난 코드 1
# 스택을 리스트로 구현
'''
pOrA = input()

ppapStack = []

for i in range(len(pOrA)):
    ppapStack.append(pOrA[i])
    if len(ppapStack)>3 and ppapStack[-4:]==['P', 'P', 'A', 'P']:
        if i==len(pOrA)-1:
            break
        else:
            ppapStack = ppapStack[:-4]+['P']

if ppapStack == ['P', 'P', 'A', 'P']:
    print('PPAP')
else:
    print('NP')
'''

# 시간 초과난 코드 2
# 스택을 문자열로 구현
'''
import sys
pOrA = sys.stdin.readline().rstrip()

ppapStr = ''

for i in range(len(pOrA)):
    ppapStr += pOrA[i]
    if len(ppapStr)>3 and ppapStr[-4:]=='PPAP':
        if i==len(pOrA)-1:
            break
        else:
            ppapStr = ppapStr[:-4]+'P'

if ppapStr == 'PPAP':
    print('PPAP')
else:
    print('NP')
'''

# 여러 조건들로 거를려고 했는데 결국 시간초과
# Cond 1. AP로 안 끝나면 NP
# Cond 2. 전체 문자열 수에서 4를 뺀 것이 3으로 나눠지지 않으면 NP 
# Cond 3. A 갯수가 전체 갯수에서 3을 나눈 몫과 동일하지 않으면 NP
# Cond 4. 중간에 'AA'가 있다면 NP
'''
import sys
pOrA = sys.stdin.readline().rstrip()

ppapStr = ''
# Cond 1.
if pOrA[-2:]!='AP':
    print('NP')
    exit()

# Cond 2.
if (len(pOrA)-4)%3!=0:
    print('NP')
    exit()

# Cond 3.
if pOrA.count('A')!=(len(pOrA)//3):
    print('NP')
    exit()

for i in range(len(pOrA)):
    ppapStr += pOrA[i]
    if len(ppapStr)>3 and ppapStr[-4:]=='PPAP':
        if i==len(pOrA)-1:
            break
        else:
            ppapStr = ppapStr[:-4]+'P'
    # Cond 4.
    elif len(ppapStr)>2 and ppapStr[-2:]=='AA':
        answer = 'NP'
        break

if ppapStr == 'PPAP':
    answer = 'PPAP'
else:
    answer = 'NP'

print(answer)

'''

# 문자열 메서드는 한계가 있어서 다시 리스트로 재도전

# 핵심은 처음 코드는 for문 내 조건문 내 수행이 '자르고 붙이고'였다면
# 정답 코드는 pop을 세 번 하는 것으로 바뀐 것
# 이 지점에서 시간 초과가 이냐 아니냐가 정해지는 것 같다

# 처음에는 틀렸습니다가 떠서 문제를 다시 읽어보고
# 'P'도 PPAP인 것을 깨닫고 조건문을 수정했더니 정답!

import sys
pOrA = sys.stdin.readline().rstrip()

ppapStack = []

for i in range(len(pOrA)):
    ppapStack.append(pOrA[i])
    if len(ppapStack)>3 and ppapStack[-4:]==['P', 'P', 'A', 'P']:
        ppapStack.pop()
        ppapStack.pop()
        ppapStack.pop()

if ppapStack==['P'] or ppapStack == ['P', 'P', 'A', 'P']:
    print('PPAP')
else:
    print('NP')