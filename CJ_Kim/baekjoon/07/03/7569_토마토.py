import sys
# 이 문제에서는 deque을 안 쓰면 시간초과가 납니다
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato_info = [[] for _ in range(H)]

# deque() vs deque([]) 차이
# deque() -> 50864KB 3360ms
# deque([]) -> 50840KB 3240ms
ripen_tomato = deque()


# 토마토 지도와 익은 토마토 덱 세팅
for h in range(H):
    for n in range(N):
        row_info = list(map(int, input().split()))
        tomato_info[h].append(row_info)
        for m in range(M):
            if tomato_info[h][n][m] == 1:
                ripen_tomato.append((m, n, h))

dm = [-1, 0, 1, 0, 0, 0]
dn = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

# 익은 토마토를 시작으로 BFS
'''
함수 처리 해보기
'''
def make_ripen():

    while ripen_tomato:
        m, n, h = ripen_tomato.popleft()

        for i in range(6):
            newM, newN, newH = m+dm[i], n+dn[i], h+dh[i]

            # 범위 내에 토마토가 아직 안 익었으면 익히기(== 이전 위치의 토마토의 것에서 날짜 수 +1) 
            if 0 <= newM < M and 0 <= newN < N and 0 <= newH < H:
                if tomato_info[newH][newN][newM] == 0:
                    ripen_tomato.append([newM, newN, newH])
                    tomato_info[newH][newN][newM] = tomato_info[h][n][m] + 1

make_ripen()

day = 0
for plate in tomato_info:
    for row in plate:
        for tomato in row:
            # 다 돌았는데 아직 익지 않은 게 있다면 결국 익지 않는 경우의 수이므로
            if tomato == 0:
                print(-1)
                exit()
        # 한 줄을 검사했을 때 가장 일자가 긴 것이 전체 토마토를 익히는 일자
        day = max(day, max(row))

# 익은 토마토가 1로 시작하므로 걸린 일자는 1 빼줘야함
print(day -1)
