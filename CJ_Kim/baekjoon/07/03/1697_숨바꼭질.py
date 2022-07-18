## python3은 통과를 못했고 pypy로는 통과했습니다.
## 시간복잡도를 줄이려고 시도해봤는데 쉽지가 않네요

subin, dongsaeng = map(int, input().split())

# 가장 큰 점은 동생 + 1이거나 수빈의 위치여야 함
# 수빈이 이동할 때 동생으로 접근하는 와중 동생 + 1의 점으로 갈 수도 있고,
# 수빈이 더 큰 점에 있을 때는 굳이 수빈 + 1, 수빈 * 2로 갈 필요가 없기 때문
end_p = dongsaeng+1 if subin<dongsaeng else subin

sum_list = [0 for _ in range(0, end_p+1)]

# BFS로 갈 수 있는 점을 가면서 시간 누적시키기
def sum_tracking(start_p):

    # deque을 쓰는 것보다 일반 리스트를 쓰는 것이 400ms 가량 단축
    sum_queue = [start_p]
    visited = []

    while sum_queue:

        cur_v = sum_queue.pop(0)

        if cur_v == dongsaeng:
            return sum_list[dongsaeng]

        # 수빈이 움직일 수 있는 점들
        for node in [cur_v-1, cur_v+1, cur_v*2]:

            # 그 중에서 범위 내에 있고 들르지 않는 곳만 누적시키기
            if 0<= node <= end_p and node not in visited:
                sum_list[node] += sum_list[cur_v] + 1
                visited.append(node)
                sum_queue.append(node)
        
print(sum_tracking(subin))