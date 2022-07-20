from sys import stdin
from collections import deque

# n, m을 공백으로 구분하여 입력받기
n, k = map(int, stdin.readline().split())
visited = [0 for _ in range(100001)]

# bfs 메서드 정의


def bfs(n):
    # deque 라이브러리 사용
    queue = deque()
    queue.append(n)
    # queue가 빌 때까지 반복
    while queue:
        n = queue.popleft()
        # n == k인 경우 해당 visited 값 반환
        if n == k:
            print(visited[n])
            exit(0)

        for i in (n-1, n+1, 2*n):
            # 범위를 벗어나지 않고, 해당 노드를 처음 방문하는 경우
            if 0 <= i <= 100000 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[n] + 1


bfs(n)
