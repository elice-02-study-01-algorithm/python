# 동일한 이름의 md파일 참고 
import sys
input = sys.stdin.readline

product, limitWeight = map(int, input().split())

productInfo = []
for _ in range(product):
    eachWeight, eachValue = map(int, input().split())
    productInfo.append([eachWeight, eachValue])
# productInfo = [[물건 무게, 물건 가치], [6, 13], [4, 8], [3, 6], [5, 12]]

# 가치값 합게 정보 담은 DP table
T = [[0 for _ in range(limitWeight+1)] for _ in range(product+1)]

def backpack(T, productInfo):
    # 물건 하나씩 들고 얘가 들어갈 수 있는지 쭉 검사하기(행 정보들)
    for i in range(len(productInfo)+1):
        # 그 물건을 가지고 무게 제한에 맞으면 업데이트하기
        for j in range(limitWeight+1):
            if i == 0 or j == 0:
                continue
            # 무게가 제한 무게보다 적으면
            if productInfo[i-1][0] <= j:
                # 이전의 정보들을 하나씩 조합해서 최댓값 갱신하기
                # 이전 행의 정보들이 최댓값들이란 것이 보장되었으므로, 그것만 가지고 검사해서 쭉 올라가면 됩니다.
                # 이전 행의 j-W무게일 때의 가치 + 현재 행에서 검사하고 있는 가방 W(j는 무게 제한)의 가치를 가지고 하나씩 검사
                T[i][j] = max(T[i-1][j-productInfo[i-1][0]]+productInfo[i-1][1], T[i-1][j])
                continue
            T[i][j] = T[i-1][j]

backpack(T, productInfo)
print(T[product][limitWeight])
'''
[   1  2  3  4  5  6  7
[
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 13, 13], 
    [0, 0, 0, 0, 8, 8, 13, 13], 
    [0, 0, 0, 6, 8, 8, 13, 14], 
    [0, 0, 0, 6, 8, 12, 13, 14]
]
'''