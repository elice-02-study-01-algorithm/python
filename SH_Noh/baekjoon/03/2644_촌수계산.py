from sys import stdin
from collections import deque
input = stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node)
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                print(check)
                queue.append(n)

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    s, e = map(int, input().split())
    for _ in range(int(input())):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    check = [0] * (n+1)
    bfs(s)
    print(check[e] if check[e] > 0 else -1)