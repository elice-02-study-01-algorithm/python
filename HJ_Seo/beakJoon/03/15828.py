'''
첫 줄에는 라우터 내부에 존재하는 버퍼의 크기를 나타내는 자연수 N이 주어진다.

둘째 줄부터 한 줄에 하나씩 라우터가 처리해야 할 정보가 주어진다. 모든 정보는 발생한 시간순으로 주어졌다고 가정한다. 
양의 정수는 해당하는 번호의 패킷이 입력으로 들어왔다는 것을 의미하고, 0은 라우터가 패킷 하나를 처리했다는 것을 의미한다. 
이때, 버퍼가 비어있을때는 0이 입력으로 들어오지 않는다. 
-1은 입력의 끝을 나타낸다.
'''


# !!!!! queue보다 deque가 훨씬 빠르고 좋다... deque에 대해하여 queue의 장점은..?..

from collections import deque
from sys import stdin
n = int(stdin.readline().strip())
buffer = deque()

while True:
    x = stdin.readline().strip()
    if x == '-1':
        break
    elif x == '0':
        buffer.popleft()
    elif len(buffer) < n:
        buffer.append(x)
    
if len(buffer) == 0:
    print('empty')
else:
    print(*buffer)


# ! 50점짜리..queue라서 느린가..?; .... X 도찐개찐.
# from sys import stdin

# n = int(input())
# lst = []

# while True:
#     x = stdin.readline()
#     if x == '-1':
#         break
#     elif x == '0':
#         lst.pop(0)
#     elif len(lst) < n:
#         lst.append(x)
        
# if len(lst) == 0:
#     print('empty')
# else:
#     print(' '.join(lst))