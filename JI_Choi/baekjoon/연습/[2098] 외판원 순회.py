from sys import stdin

# n 입력받기
n = int(stdin.readline())

# 비용행렬 입력받기
info = []
for i in range(n):
    data = list(map(int, stdin.readline().split()))
    info.append(data)

# 초기 설정
INF = int(1e9)
dp = [[INF] * (1<<n) for _ in range(n)]

# DFS
def dfs(x, visited):
    # 모든 도시를 방문한 경우
    if visited == (1<<n) - 1:
        # 출발점으로 가는 경로가 존재하는 경우
        if info[x][0]:
            return info[x][0]
        # 존재하지 않는 경우
        else:
            return INF
    
    # 최소비용이 계산되어 있는 경우
    if dp[x][visited] != INF:
        return dp[x][visited]
    
    # 모든 도시를 탐방
    for i in range(1, n):
        # x도시에서 i도시로 가는 경로가 없는 경우
        if not info[x][i]:
            continue 
        # 이미 방문한 도시인 경우
        if visited & (1<<i):
            continue
        # 최소비용 가능성이 있는 값 구하기
        pseudo_value = info[x][i] + dfs(i, visited | 1<<i)

        # 기존에 저장된 값보다 작은 경우
        if dp[x][visited] > pseudo_value:
            # dp값 최신화
            dp[x][visited] = pseudo_value

    return dp[x][visited]

print(dfs(0, 1))







