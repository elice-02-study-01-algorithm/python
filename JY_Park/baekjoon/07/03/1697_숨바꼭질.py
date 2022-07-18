from collections import deque
n, k = map(int,input().split())

# 계산된 결과를 저장하기 위해서 리스트 초기화
d = [0] * 100001

def bfs():
    queue = deque([n])

    while queue:
        cur = queue.popleft()
        if cur == k:
            return d[cur]
        # 현재 위치에서 갈 수 있는 위치
        for i in (cur+1, cur-1, cur*2):
            if i >= 0 and i <= 100000 and d[i] == 0:
                # d[i]: 새로 이동한 위치의 경우, d[cur]: 현재 경우
                d[i] = d[cur] + 1
                queue.append(i)

print(bfs())