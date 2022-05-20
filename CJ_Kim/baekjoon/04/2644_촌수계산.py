# 아직 주석을 추가하지 못해서 스터디 이후 주석 추가하겠습니다
from collections import deque

total = int(input())
per1, per2 = map(int, input().split())
relNum = int(input())

familyGraph = {}
for _ in range(relNum):
    parent, child = map(int, input().split())
    if parent in familyGraph:
        familyGraph[parent].append(child)
        if child in familyGraph:
            familyGraph[child].append(parent)
        else:
            familyGraph[child] = [parent]
    else:
        familyGraph[parent] = [child]
        if child in familyGraph:
            familyGraph[child].append(parent)
        else:
            familyGraph[child] = [parent]

def BFS(root):
    queue = deque()
    queue.append(root)
    while queue:
        root = queue.popleft()
        for node in familyGraph[root]:
            if check[node] == 0:
                check[node] = check[root] + 1
                queue.append(node)

check = [0]*(total+1)
BFS(per1)

print(check[per2] if check[per2]>0 else -1)