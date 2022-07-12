# 50점짜리
'''
# 큐문제라서 당연히 큐로 시도해보았음
from queue import Queue
buffer = int(input())
bufferQ = Queue()

while True:
    info = int(input())
    if info == -1:
        break
    elif info == 0:
        bufferQ.get()
    # 버퍼의 크기보다 정보가 적게 있을 때만 위치시키기
    elif bufferQ.qsize()<buffer:
        bufferQ.put(info)
if bufferQ.qsize()==0:
    print('empty')
else:
    while bufferQ.qsize()>0:
        print(bufferQ.get())

# 아래의 코드와 로직은 다를 게 없어보이는 데 
# 아마 나머지 50점은 시간초과로 추측됨
'''
# 100점 짜리

# 50점을 맞기도 했고, 
# 채점 중 퍼센트가 매우 느리게 올라가는 것을 확인하여 재시도
import sys

buffer = int(sys.stdin.readline())
# 큐를 리스트로 구현
bufferList = []

while True:
    info = int(sys.stdin.readline())
    if info == -1:
        break
    elif info == 0:
        bufferList.pop(0)
    elif len(bufferList)<buffer:
        bufferList.append(info)

if len(bufferList)==0:
    print('empty')
else:
    print(*bufferList)