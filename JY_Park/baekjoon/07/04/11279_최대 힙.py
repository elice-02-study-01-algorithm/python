from sys import stdin
input = stdin.readline
import heapq

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)


# 처음
# heapq.heappush(heap, (-x,x))
# -> heap을 tuple로 구성했을 때 앞 숫자로 정렬하므로 정렬 기준 값은 첫번 째 원소로 하고 뒤는 원래 값 넣었음.
# 그리고 pop할 때 인덱싱했음. heapq.heappop(heap)[1]

# 수정한 방법
# heap에 값을 - 붙여서 넣고 pop해서 -붙여줌.