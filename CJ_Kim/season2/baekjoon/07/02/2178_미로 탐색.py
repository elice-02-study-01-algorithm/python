import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())

'''
[[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
형태의 2차원 배열 맵 짜기
'''
miro_map = [[] for _ in range(row)]
for i in range(row):
    elements = str(input()).strip()
    for element in elements:
        miro_map[i].append(int(element))

# 로봇청소기 방식
# d/방향/(dr, dc): 0/북/(-1, 0), 1/동/(0, 1), 2/남/(1, 0), 3/서/(0, -1)
#    -1
# -1 기준 +1
#    +1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방문했으면 1, 아니면 0
visited = [[0 for _ in range(col)] for _ in range(row)]
# 방문한 곳마다 가게된 거리를 누적해서 기록, 시작은 1
distance = [[0 for _ in range(col)] for _ in range(row)]
distance[0][0] = 1

def BFS(vertex_info, x, y):
    # 큐에 한 위치 담기
    queue = [[x, y]]
    visited[x][y] == 1
    
    while queue:
        # 한 위치 꺼내서
        r, c = queue.pop(0)
        # 그 위치에서 사방으로 가기
        for i in range(4):
            newR, newC = r+dr[i], c+dc[i]
            # 다음으로 갈 곳이 범위 내에 있냐
            if 0<=newR<row and 0<=newC<col:
                # 다음으로 갈 곳이 갈 수 있는 곳이냐/방문하지 않는 곳이냐
                if vertex_info[newR][newC] == 1 and visited[newR][newC] == 0:
                    # 거리는 이것 위치의 그것에서 1 더하기
                    distance[newR][newC] = distance[r][c] + 1
                    # 방문했으면 1로 바꿔주기
                    visited[newR][newC] = 1
                    # 큐에 다음 위치 담기
                    queue.append([newR, newC])

# 너비 우선 탐색으로 distance 넣어주기
BFS(miro_map, 0, 0)

'''
4 6
101111
101010
101011
111011
의 경우
distance = 
[
    [3, 0, 9, 10, 11, 12], 
    [2, 0, 8, 0, 12, 0], 
    [3, 0, 7, 0, 13, 14], 
    [4, 5, 6, 0, 14, 15]
]
4 6
110110
110110
111111
111101
의 경우
[
    [3, 2, 0, 8, 9, 0], 
    [2, 3, 0, 7, 8, 0], 
    [3, 4, 5, 6, 7, 8], 
    [4, 5, 6, 7, 0, 9]
]
2 25
1011101110111011101110111
1110111011101110111011101
의 경우
[
    [3, 0, 5, 6, 7, 0, 11, 12, 13, 0, 17, 18, 19, 0, 23, 24, 25, 0, 29, 30, 31, 0, 35, 36, 37], 
    [2, 3, 4, 0, 8, 9, 10, 0, 14, 15, 16, 0, 20, 21, 22, 0, 26, 27, 28, 0, 32, 33, 34, 0, 38]
]
'''
print(distance[row-1][col-1])