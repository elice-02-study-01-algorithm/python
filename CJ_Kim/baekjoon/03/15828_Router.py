# 50점짜리
'''
from queue import Queue
buffer = int(input())
bufferQ = Queue()

while True:
    info = int(input())
    if info == -1:
        break
    elif info == 0:
        bufferQ.get()
    elif bufferQ.qsize()<buffer:
        bufferQ.put(info)
if bufferQ.qsize()==0:
    print('empty')
else:
    while bufferQ.qsize()>0:
        print(bufferQ.get())
'''
# 100점 짜리
import sys

buffer = int(sys.stdin.readline())
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