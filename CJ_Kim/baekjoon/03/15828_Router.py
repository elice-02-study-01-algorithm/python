# 50점짜리
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