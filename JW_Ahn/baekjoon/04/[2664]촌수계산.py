import sys

# find1 으로 촌수 +1 하면서 dfs
def dfs(find1):
    for f in graph[find1]:
        if visited[f] == 0:
            visited[f] = visited[find1] + 1
            dfs(f)

n = int(sys.stdin.readline())
find1, find2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(find1)

# 방문하지 않았다면 친척 관게가 없음 => -1 출력
print(visited[find2] if visited[find2] > 0 else -1)
