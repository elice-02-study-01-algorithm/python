##################
# TRY I ##########
##################
# 시간 초과!
'''
## python3은 통과를 못했고 pypy로는 통과했습니다.
## 시간복잡도를 줄이려고 시도해봤는데 쉽지가 않네요
from collections import deque
subin, dongsaeng = map(int, input().split())

# 가장 큰 점은 동생 + 1이거나 수빈의 위치여야 함
# 수빈이 이동할 때 동생으로 접근하는 와중 동생 + 1의 점으로 갈 수도 있고,
# 수빈이 더 큰 점에 있을 때는 굳이 수빈 + 1, 수빈 * 2로 갈 필요가 없기 때문

sum_list = [0 for _ in range(100001)]

# BFS로 갈 수 있는 점을 가면서 시간 누적시키기
def sum_tracking(start_p):

    # deque을 쓰는 것보다 일반 리스트를 쓰는 것이 400ms 가량 단축
    sum_queue = deque([start_p])
    visited = []

    while sum_queue:

        cur_v = sum_queue.popleft()

        if cur_v == dongsaeng:
            return sum_list[dongsaeng]

        # 수빈이 움직일 수 있는 점들
        for node in (cur_v-1, cur_v+1, cur_v*2):

            # 그 중에서 범위 내에 있고 들르지 않는 곳만 누적시키기
            if 0<= node <= 100000 and node not in visited:
                sum_list[node] += sum_list[cur_v] + 1
                visited.append(node)
                sum_queue.append(node)
        
print(sum_tracking(subin))
'''

##################
# TRY II #########
##################
# I과의 차이점은 visited을 따로 두지 않고 조건문에서 
# node not in visited -> sum_list[node]==0
# x in s -> O(n)  list[x](get item) -> O(1) 
# operation 시간복잡도때문에 발생한 시간초과인 듯합니다.
# 앞으로 조건문 작성할 때 최대한 비교(get item)로 주기!
# 34692 KB 160 ms
'''
from collections import deque
subin, dongsaeng = map(int, input().split())

sum_list = [0 for _ in range(100001)]

# BFS로 갈 수 있는 점을 가면서 시간 누적시키기
def sum_tracking(start_p):

    # deque을 쓰는 것보다 일반 리스트를 쓰는 것이 400ms 가량 단축
    sum_queue = deque([start_p])

    while sum_queue:

        cur_v = sum_queue.popleft()

        if cur_v == dongsaeng:
            return sum_list[dongsaeng]

        # 수빈이 움직일 수 있는 점들
        for node in (cur_v-1, cur_v+1, cur_v*2):

            # 그 중에서 범위 내에 있고 들르지 않는 곳만 누적시키기
            if 0<= node <= 100000 and sum_list[node]==0:
                sum_list[node] += sum_list[cur_v] + 1
                
                sum_queue.append(node)
        
print(sum_tracking(subin))
'''
##################
# TRY III ########
##################
# 34760 KB 156 ms
# II와의 차이는 end_p를 준 것, 메모리를 줄이려고 한 것 이지만 시간이 줄어서 의아

from collections import deque
subin, dongsaeng = map(int, input().split())

# 가장 큰 점은 동생 + 1이거나 수빈의 위치여야 함
# 수빈이 이동할 때 동생으로 접근하는 와중 동생 + 1의 점으로 갈 수도 있고,
# 수빈이 더 큰 점에 있을 때는 굳이 수빈 + 1, 수빈 * 2로 갈 필요가 없기 때문

end_p = dongsaeng+1 if subin<dongsaeng else subin

sum_list = [0 for _ in range(end_p+1)]

# BFS로 갈 수 있는 점을 가면서 시간 누적시키기
def sum_tracking(start_p):

    # deque을 쓰는 것보다 일반 리스트를 쓰는 것이 400ms 가량 단축
    sum_queue = deque([start_p])

    while sum_queue:

        cur_v = sum_queue.popleft()

        if cur_v == dongsaeng:
            return sum_list[dongsaeng]

        # 수빈이 움직일 수 있는 점들
        for node in (cur_v-1, cur_v+1, cur_v*2):

            # 그 중에서 범위 내에 있고 들르지 않는 곳만 누적시키기
            if 0<= node <= end_p and sum_list[node]==0:
                sum_list[node] += sum_list[cur_v] + 1
                
                sum_queue.append(node)
        
print(sum_tracking(subin))