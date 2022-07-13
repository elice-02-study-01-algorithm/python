from collections import deque
n, m, v = map(int, input().split())

# 1번부터 시작
graph = [[] for i in range(n + 1)]
check_visit = [False] * (n + 1)

# 그래프에 입력값을 넣어준다. 양방향인거 고려해서!
# [[], [1, 2, 3], [1, 4], [1, 4], [2, 3, 4]]
for i in range(m):
    a, b = map(int, input().split())        
    graph[a].append(b)
    graph[b].append(a)
# 작은거부터 들르기
for i in range(len(graph)):
    graph[i].sort()

dfs_result = []

def dfs(start):
    dfs_result.append(start)
    # start 지점에 방문했다!    
    check_visit[start] = True
    for i in graph[start]:
        if check_visit[i] == False:
            dfs(i)
            check_visit[i] = True
dfs(v)

check_visit = [False] * (n + 1)

bfs_result = []

def bfs(start):
    # start 지점에 방문했다!
    check_visit[start] = True
    deq = deque([start])
    while(deq):
        cur = deq.popleft()
        bfs_result.append(cur)
        for i in graph[cur]:
            if check_visit[i] == False:
                deq.append(i)
                check_visit[i] = True
bfs(v)

for i in range(len(dfs_result)):
    print(dfs_result[i], end=" ")
print()
for i in range(len(bfs_result)):
    print(bfs_result[i], end=" ")