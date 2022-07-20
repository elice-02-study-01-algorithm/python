# 수빈이 위치 N, 동생 위치 K
# 수빈이는 걷거나 순간이동
# 걸을 땐 X +- 1
# 순간이동은 2*X 위치로
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은?

from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque([subin])
    while True:
        current = q.popleft()

        if current == brother:
            print(dist[current])
            break

        for next in (current - 1, current + 1, current * 2):
            if 0 <= next <= 100000 and dist[next] == 0:
                dist[next] = dist[current] + 1 
                q.append(next)

if __name__ == "__main__":
    subin, brother = map(int, input().split())
    # 수빈이로부터 각 위치의 거리를 저장하는 배열
    dist = [0] * 100001
    bfs()
