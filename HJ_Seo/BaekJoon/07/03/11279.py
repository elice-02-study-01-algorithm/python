from sys import stdin
import heapq

x = []

n = int(input())

# 큰 수를 뽑아내야하니 - 붙이기!
while n != 0:
    do = stdin.readline().strip()
    
    if do == '0':
        if len(x) != 0:
            print(-heapq.heappop(x))
        else:
            print(0)
    else:
        heapq.heappush(x,-int(do))

    n -= 1