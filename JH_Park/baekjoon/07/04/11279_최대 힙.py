import heapq
import sys

q = []

n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not q:
            print(0)    
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (-x, x))


# 참고
# https://www.daleseo.com/python-heapq/