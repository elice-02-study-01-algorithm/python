import sys
input = sys.stdin.readline

N, K = map(int, input().split())
walkDic = {}
bikeDic = {}
findMax = []
for i in range(1, N+1):
    w_t, w_m, d_t, d_m  = map(int, input().split())
    walkDic[i] = [w_t, w_m]
    bikeDic[i] = [d_t, d_m]
    findMax.append((i, max(w_m, d_m)))

def makeMax():
    resultDic = {1: [walkDic[1], bikeDic[1]]}
    return
print(walkDic)
print(bikeDic)

"""
~~0. 시간당 모금 비율을 계산하기~~
1. 최대 모금액을 가진 것을 확정지은 다음 다른 것들을 맞춰나가기
2. 제한 시간 경우의 수를 먼저 모으고 그 중에서 최댓값 찾기
"""
