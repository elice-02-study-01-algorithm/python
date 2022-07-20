from collections import deque

MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())

q = deque()
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        break
    for i in (cur - 1, cur + 1, cur * 2):
        if 0 <= i <= MAX and not dist[i]:
            dist[i] = dist[cur] + 1
            q.append(i)