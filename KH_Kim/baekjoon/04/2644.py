# 백준
# 2644번 : 촌수
# 그래프 이론, 그래프 탐색, BFS, DFS

# *
# n: 전체 사람의 수
# a, b: 촌수 계산 서로다른 사람의 번호
# m: 부모 자식 관계의 개수
# x,y 부모 자식 관계 (부모, 자식)

def dfs(v, num):
    num += 1
    visited[v] = True

    if v == B:
        result.append(num)

    for i in tree[v]:
        if not visited[i]:
            dfs(i, num)


if __name__ == '__main__':
    # n, a,b, m 입력
    N = int(input())
    A, B = map(int, input().split())
    M = int(input())
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2D 리스트)
    tree = [[] for _ in range(N+1)]
    # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1D 리스트)
    visited = [False] * (N+1)
    result = []

    # 부모 자식 관계 입력
    for i in range(M):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)

    # print('tree')
    # print(tree)
    ## [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

    dfs(A, 0)
    if len(result) == 0:
        print(-1)
    else:
        # print(result)
        # [4]
        print(result[0]-1)

        # print(visited)
        ## [False, True, True, True, False, False, False, True, True, True]
