'''
#시간초과

import sys
input = sys.stdin.readline

sanggeun_str = input().strip()
bomb_str = input().strip()

char_stack = ''
for char in sanggeun_str:
    char_stack += char
    if char == bomb_str[-1]:

        if len(char_stack)>=len(bomb_str) and char_stack[-1-(len(bomb_str))+1:] == bomb_str:
            bomb_index = 0
            new_stack = char_stack[:-(len(bomb_str))]
            char_stack = new_stack

if char_stack == '':
    print('FRULA')
else:
    print(char_stack)
'''

'''
# 42020KB, 748ms
import sys
input = sys.stdin.readline

sanggeun_str = input().strip()
bomb_str = input().strip()

char_stack = []
for char in sanggeun_str:
    char_stack.append(char)
    if char == bomb_str[-1]:
        if len(char_stack)>=len(bomb_str) and char_stack[-1-(len(bomb_str))+1:] == list(bomb_str):
            bomb_index = 0
            while bomb_index < len(bomb_str):
                bomb_index += 1
                char_stack.pop()

if char_stack == []:
    print('FRULA')
else:
    print(''.join(char_stack))
'''

'''
mirkovC4 nizCC44
       👆
    항상 여기 끝에서 검사합니다.
C4
'''

# 42024KB 568ms

# 위의 것과 다른 점은 
# 위는 검사 후 앞의 stack에서 삭제 할 때 폭발 문자열 수만큼 pop을 한 것이고,
# 아래는 slice한 것에 대해 del을 쓴 것입니다.
import sys
input = sys.stdin.readline

sanggeun_str = input().strip()
bomb_str = input().strip()

# 주어진 문자열을 돌면서 왼쪽부터 떼내어 하나씩 넣는 곳 
char_stack = []

for char in sanggeun_str:
    char_stack.append(char)
    # 방금 넣었던 것과 폭발 문자열의 오른쪽 끝과 비교하여 먼저 걸러주기
    # 폭발 문자열과 슬라이스한 것과 비교를 먼저 안 하는 이유는
    # 슬라이스한 것도 시간이 많이 들고, 더불어 왼쪽 스택에서 폭발 문자열 수만큼 안 들어올 경우도 있기에,
    # 시간 절약을 위해 간단한 연산으로 먼저 빠르게 걸러주었습니다.
    if char == bomb_str[-1]:
        # 왼쪽에 쌓인 스택이 폭발 문자열 수보다 같거나 크고, 슬라이싱한 것과 동일할 때 제거해주기
        if len(char_stack)>=len(bomb_str) and char_stack[-(len(bomb_str)):] == list(bomb_str):
            del char_stack[-(len(bomb_str)):]

if char_stack == []:
    print('FRULA')
else:
    print(''.join(char_stack))
