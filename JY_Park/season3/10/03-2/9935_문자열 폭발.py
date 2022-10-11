'''
아이디어 정리
1. 폭발 문자열의 크기만큼 꺼내서 큐나 리스트에 넣어둠.
2. 리스트 join해서 폭발 문자열이랑 같으면 큐 비우고 다시 하나씩 빼냄.
3. 다르면 선입선출 한 개 하고 새로 꺼내옴.

queue1 = [m,i,r,k,o,v,C,4,n,i,z,C,C,4,4]
queue2 = []

temp = ''

'''

'''
from sys import stdin
from collections import deque
input = stdin.readline

queue1 = deque(input().strip())
queue2 = deque()
bomb = input().strip()

# ''.join(queue1).find(bomb) != -1 / find 쓰면 시간초과
while True:
    temp = ''
    # 반복 전 길이 체크
    memory_len = len(queue1)

    while True:
        temp += queue1.popleft()
        # print(temp)

        if len(temp) == len(bomb):
            if temp == bomb:
                temp = ''
            else:
                queue2.append(temp[0])
                temp = temp[1:]

        if len(queue1) == 0:
            break
        # print(temp, queue1, queue2)

    # print(temp)
    if temp: 
        for i in temp:
            queue2.append(i)
    
    # print(queue1, queue2)
    queue1 = queue2
    queue2 = deque()

    # 다 돌았는데 길이가 그대로이면 끝
    if memory_len == len(queue1) or not queue1:
        break

print(''.join(queue1)) if queue1 else print('FRULA')
'''

'''
abcdefg
dca
'''

'''
from sys import stdin
from collections import deque
input = stdin.readline

queue1 = deque(input().strip())
bomb = input().strip()

while True:
    temp = ''
    # 반복 전 길이 체크
    memory_len = len(queue1)

    for _ in range(len(queue1)):
        temp += queue1.popleft()

        if len(temp) == len(bomb):
            if temp == bomb:
                temp = ''
            else:
                queue1.append(temp[0])
                temp = temp[1:]

    if temp: 
        for i in temp:
            queue1.append(i)
    
    if memory_len == len(queue1) or not queue1:
        break

print(''.join(queue1)) if queue1 else print('FRULA')
'''

# 처음부터 넣어서 시작하지 말고 하나씩 넣다가 길이가 폭탄 길이보다 길고 끝 문자가 같을 때 확인해서
# 같으면 터트리고 아니면 push
from sys import stdin
input = stdin.readline

word = input().strip()
stack = []
bomb = input().strip()
bomb_length = len(bomb)

for w in word:
    stack.append(w)

    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]
    
print(''.join(stack)) if stack else print('FRULA')