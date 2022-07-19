import queue as q
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
q = q.Queue()

while True:
    m = int(input())
    # input이 -1인 경우
    if m == -1:
        break
    # input이 0인 경우
    elif m == 0:
        q.get()
    # input이 -1, 0 이외의 값인 경우
    else:
        if q.qsize() < n:
            q.put(m)

if q.qsize() == 0:
    print("empty")
else:
    print(*list(q.queue))
