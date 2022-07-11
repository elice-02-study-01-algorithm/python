# 입력 변수 받기
N, M, V = map(int, input().split())

# 인접 영행렬 생성
matrix=[[0] * (N + 1) for i in range(N + 1)]

# 방문한 곳 체크를 위한 배열 선언
visited = [0] * (N + 1)

# 입력 받는 두 값에 대해 영행렬에 1 삽입
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(V):
    # 방문한 곳은 1 넣기
    visited[V] = 1
    
    print(V, end=' ')
    
    # 재귀 함수 선언(V와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)
    for i in range(1,N+1):
        if(visited[i]==0 and matrix[V][i]==1):
            dfs(i)

            
def bfs(V):
    # 방문해야 할 곳을 순서대로 넣을 큐
    queue = [V]
    
    # dfs 를 완료한 visited 배열(1로 되어있음)에서 0으로 방문체크
    visited[V] = 0
    
    # 큐 안에 데이터가 없을 때 까지
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N + 1):
            if(visited[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)