from typing import List
# from collections import deque
# n: 정사각형 크기 m: 알고싶은 분
def firing(fires, arr, n):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    now_fires = fires[:]
    for x, y in now_fires:
        x, y = x - 1, y - 1
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if [nx + 1, ny + 1] not in fires:
                    fires.append([nx + 1, ny + 1])
    for x, y in fires:
        x, y = x - 1, y - 1
        arr[x][y] += 1
    return fires, arr

def icing(ices, arr, n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    now_ices = ices[:]
    for x, y in now_ices:
        x, y = x - 1, y - 1
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if [nx + 1, ny + 1] not in ices:
                    ices.append([nx + 1, ny + 1])
    for x, y in ices:
        x, y = x - 1, y - 1
        arr[x][y] -= 1
    return ices, arr

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[0] * n for _ in range(n)]
    for minute in range(1, m + 1):
        fires, answer = firing(fires, answer, n)
        # print(answer)
        ices, answer = icing(ices, answer, n)
        print(answer)
    return answer
    
print(solution(3, 2, [[1, 1]], [[3, 3]]))
# [[2, 2, 0], [2, 1, -1], [0, -1, -1]]
print(solution(5, 3, [[5, 5], [1, 3], [5, 2]], [[1, 5], [3, 2]]))