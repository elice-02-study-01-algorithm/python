def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return 
    
    for i in range(1, n+1):
        # 아직 방문하지 않았고 리스트가 비어있거나 차있다면 큰 값보다 i가 클 경우
        if i not in s and (not s or i >= s[-1]):
            s.append(i)
            dfs()
            s.pop()

n, m = map(int, input().split())
s = []

dfs()