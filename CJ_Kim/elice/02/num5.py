import sys
sys.setrecursionlimit(10000)
ppl, sul = map(int, input().split())
arrowList = [[]]
for _ in range(ppl):
    left, right = map(int, input().split())
    arrowList.append([left, right])
    

def DFS(list, p, visited):
    visited.append(p)
    
    if list[p][0] not in visited:
        visited = DFS(list, list[p][0], visited)
    if list[p][1] not in visited:
        visited = DFS(list, list[p][1], visited)
    return visited

visited= []
visitedAnswer = DFS(arrowList, sul, visited)
print(ppl-len(visitedAnswer))

import sys
sys.setrecursionlimit(10000)
ppl, sul = map(int, input().split())
arrowList = [[]]
for _ in range(ppl):
    left, right = map(int, input().split())
    arrowList.append([left, right])
    

# def DFS(list, p, visited):
#     visited.append(p)
    
#     if list[p][0] not in visited:
#         visited = DFS(list, list[p][0], visited)
#     if list[p][1] not in visited:
#         visited = DFS(list, list[p][1], visited)
#     return visited
    
def DFS(list, p):
    stack, visited = [p], []
    while stack:
        
        node = stack.pop()
        if list[node][0] in visited:
            continue
        visited.append(list[node][0])
        if list[node][1] in visited:
            continue
        visited.append(list[node][1])
        for leftNright in list[node]:
            stack.append(leftNright)
    return visited


visited= []
visitedAnswer = DFS(arrowList, sul)
print(ppl-len(visitedAnswer))
