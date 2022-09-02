import heapq
import sys

q = []
n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)