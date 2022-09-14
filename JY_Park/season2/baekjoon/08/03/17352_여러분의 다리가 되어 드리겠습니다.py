'''
풀이2 : 분리집합을 통해 각 집합을 갱신하고, 
        집합에 포함되지 않는 섬과 집합에 포함되는 섬을 하나씩 출력한다.
'''

import sys
# from collections import deque
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
# 경로 압축 방법
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기(union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(n+1)]

# Union 연산을 각각 수행
for _ in range(n-2):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# print(parent)

for i in range(1, n+1):
    # 다른 섬이랑 연결되어 있지 않다.
    if i == parent[i]:
        parent1 = i
for i in range(1, n+1):
    # 앞에 선택한 섬이랑 연결되어 있지 않은 
    if parent[i] != parent1:
        parent2 = i
        break
print(parent1, parent2)

# graph = [[]*(n+1) for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(n-2):
#     x, y = list(map(int, input().split()))
#     graph[x].append(y)
#     graph[y].append(x)

# def bfs(v):
#   land = [v]
#   visited[v] = True
#   queue = deque(graph[v])

#   while queue:
#     cur = queue.popleft()
#     land.append(cur)
#     visited[cur] = True

#     for i in graph[cur]:
#       if not visited[i]:
#         queue.append(i)

#   return land

# result = []
# for i in range(1, n+1):
#   if not visited[i]:
#     result.append(bfs(i))

# print(result[0][0], result[1][0])



# def dfs(v):
#     visited[v] = True
#     for i in range(1,n+1):
#         if not visited[v]:
#             dfs(v)