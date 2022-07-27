from sys import stdin
import heapq

# n 입력받기
n = int(stdin.readline())
arr = []

for _ in range(n):
    num = int(stdin.readline())
    # num 값이 자연수인 경우
    if num:
        heapq.heappush(arr, (-1) * num)
    # num 값이 0인 경우
    else:
        # 배열에 원소가 존재하는 경우
        if arr:
            print((-1) * heapq.heappop(arr))
        # 빈 배열인 경우
        else:
            print(0)

    