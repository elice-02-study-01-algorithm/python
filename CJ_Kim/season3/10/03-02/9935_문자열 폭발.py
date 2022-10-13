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
C4
'''

# 42024KB 568ms

# 
import sys
input = sys.stdin.readline

sanggeun_str = input().strip()
bomb_str = input().strip()

char_stack = []

for char in sanggeun_str:
    char_stack.append(char)
    if char == bomb_str[-1]:
        if len(char_stack)>=len(bomb_str) and char_stack[-(len(bomb_str)):] == list(bomb_str):
            del char_stack[-(len(bomb_str)):]

if char_stack == []:
    print('FRULA')
else:
    print(''.join(char_stack))
