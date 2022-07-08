from collections import deque

total = int(input())
# 구해야하는 사람 둘 == per1, per2
per1, per2 = map(int, input().split())
relNum = int(input())

# 양방향 가족그래프 생성
# 모임 때 설명했듯이, 이 부분에서 시간을 많이 잡아먹는 듯함
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

# 너비우선탐색 진행
def BFS(root):
    # root == 시작하는 위치
    queue = deque()
    queue.append(root)
    while queue:
        root = queue.popleft()
        for node in familyGraph[root]:
            # 지나가지 않은 곳이면 지나가면서 길이 하나씩 추가하면서 입력
            if check[node] == 0:
                check[node] = check[root] + 1
                queue.append(node)

# 경로 저장하는 리스트
check = [0]*(total+1)

# per1과 관련되는 모든 촌수를 check에 계산
BFS(per1)

# per2와의 거리 출력
print(check[per2] if check[per2]>0 else -1)