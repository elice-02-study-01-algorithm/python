# https://www.acmicpc.net/problem/11279

###########
## TRY I ##
###########
# 37788 KB 160 ms
from sys import stdin
import heapq
input = stdin.readline

operation = int(input())
heap = []

for _ in range(operation):
    # 음수로 전환하여 큰 수부터 sort하도록 만들기
    this_num = (-1)*int(input())
    if this_num==0:
        print((-1)*heapq.heappop(heap) if len(heap)!=0 else 0)
    else:
        heapq.heappush(heap, this_num)

###########
## TRY II #
###########
# 우선순위를 따로 담고 튜플로 넣기
# 47004 KB 184 ms
'''
from sys import stdin
import heapq
input = stdin.readline

operation = int(input())
heap = []

for _ in range(operation):
    this_num = int(input())
    if this_num==0:
        print(heapq.heappop(heap)[1] if len(heap)!=0 else 0)
    else:
        heapq.heappush(heap, ((-1)*this_num, this_num))
'''