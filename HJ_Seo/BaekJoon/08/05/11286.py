import heapq
from sys import stdin
order = int(stdin.readline().strip())
over_lst = []
under_lst = []
# lst = []
for _ in range(order):
    n = int(stdin.readline().strip())
    if n == 0:
        if over_lst and under_lst:
            if over_lst[0] < under_lst[0]:
                # lst.append(heapq.heappop(over_lst))
                print(heapq.heappop(over_lst))
            else:
                # lst.append(-heapq.heappop(under_lst))
                print(-heapq.heappop(under_lst))
        elif over_lst:
            # lst.append(heapq.heappop(over_lst))
            print(heapq.heappop(over_lst))
        elif under_lst:
            # lst.append(-heapq.heappop(under_lst))
            print(-heapq.heappop(under_lst))
        else:
            # lst.append(0)
            print(0)
    elif n > 0:
        heapq.heappush(over_lst,n)
    else:
        heapq.heappush(under_lst,abs(n))
 