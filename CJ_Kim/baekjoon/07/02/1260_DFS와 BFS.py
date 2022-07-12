import sys 
from collections import deque
input = sys.stdin.readline

# 초기값 받기
N, M, V = map(int, input().split())
m_info = [[] for _ in range(N+1)]

# 그래프 만들기
for _ in range(M):
    V1, V2 = map(int, input().split())
    m_info[V1].append(V2)
    m_info[V2].append(V1)

# 그래프 정점들 정렬하기
for node in m_info:
    node.sort()

# DFS는 stack을 이용해 가장 작은 것이 먼저 나올 수 있도록 정렬해서 넣는다
# 재귀가 더 빠름 268ms ✓
def DFS(vertex_info, start_v):
    visited=[]
    stack = [start_v]
    while stack:
        cur_v = stack.pop()
        if cur_v not in visited:
            visited.append(cur_v)
            if vertex_info[cur_v]:
                stack += sorted(vertex_info[cur_v], reverse=True)
    return visited

# BFS는 deque를 이용해 한 정점당 갈 수 있는 곳을 전부 탐색한 뒤 다음 정점으로 넘어간다.
def BFS(vertex_info, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)
    while queue:
        cur_v = queue.popleft()
        for node in vertex_info[cur_v]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    return visited

'''40ms 더 느린 코드
예상컨데 deque를 쓰지 않고 동시에 +=를 써서 차이가 나는 듯
def BFS(root):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += nodeInfo[node]
    return visited
'''

print(*DFS(m_info, V))     
print(*BFS(m_info, V)) 