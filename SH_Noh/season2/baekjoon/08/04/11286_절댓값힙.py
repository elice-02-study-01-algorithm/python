from heapq import heappop, heappush
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x != 0:
        heappush(heap, (abs(x), x))
    else:
        if len(heap) == 0:
            print(f"0\n")
        else:
            print(f"{heappop(heap)[1]}\n")
