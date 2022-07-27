from sys import stdin
input = stdin.readline
from collections import deque

n = input().strip()
m = int(input())

queue_left = [i for i in n]
queue_right = deque([])

# cursor = len(n)

for i in range(m):
    command = input()
    if command[0] == "L":
        if queue_left:
            cur = queue_left.pop()
            queue_right.append(cur)
    elif command[0] == "D":
        if queue_right: 
            cur = queue_right.pop()
            queue_left.append(cur)
    elif command[0] == "B":
        if queue_left:
            queue_left.pop()
    elif command[0] == "P":
        queue_left.append(command[2])
    # print(queue_left,queue_right)

queue_right.reverse()
print(''.join(queue_left)+''.join(queue_right))

# cursor의 위치를 문자열 길이만큼에서 시작해서 cursor를 옮기면서 값을 넣으려고 했지만 잘 안됨.
# cursor = len(n)  -> 시간초과
# 그래서 자료구조 사용해야겠다고 생각했고
# 처음엔 left, right 둘 다 deque로 구현했는데 left에서 값을 선택하는게 stack을 사용하는게 적절할 것 같아서

# 반례
#INPUT
# dmiqn
# 10
# P m
# P n
# D
# D
# L
# L
# P a
# P s
# D
# D

#ANSWER
# dmiqnasmn