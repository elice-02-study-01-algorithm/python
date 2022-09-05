# https://www.acmicpc.net/problem/14427
import sys
input = sys.stdin.readline
VALUE, INDEX = 0, 1

seqLen = int(input())
# 5
seq = [0]+list(map(int, input().strip().split()))
# 5 4 3 2 1
tree = [[0, 0]]*(3*seqLen)
# 2로 하면 런타임 에러 발생(IndexError)
# 3인 경우: 57300KB, 1696ms
# 4인 경우: 58084KB, 1436ms

def init(node, start, end):
    if (start==end):
        tree[node] = [seq[start], start]
    else:
        # 아래 레벨로 내려가서 반으로 잘라 배분하는 작업
        mid = (start+end)//2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)

        smaller_node = node*2
        if tree[node*2][VALUE] > tree[node*2+1][VALUE]:
            smaller_node = node*2+1
        
        # 맨 아래가 아닌 위의 레벨인 경우는 부분 중 최솟값을 배치해야 하므로
        tree[node] = [tree[smaller_node][VALUE], tree[smaller_node][INDEX]]

init(1, 1, seqLen)

'''
print(tree)
# 5 4 3 2 1
[[0, 0], 
[1, 5], 
[3, 3], [1, 5], 
[4, 2], [3, 3], [2, 4], [1, 5], 
[5, 1], [4, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
[0, 0], [0, 0], [0, 0], [0, 0]]
'''
'''
# 10 9 8 7 6
[[0, 0], 
[6, 5], - 10 9 8 7 6
[8, 3], [6, 5], - 10 9 8 / 7 6
[9, 2], [8, 3], [7, 4], [6, 5], - 10 9 / 8 / 7 / 6
[10, 1], [9, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 
[0, 0], [0, 0], [0, 0], [0, 0]]
'''

query = int(input())

def update(node, left, right, index, value):
    # index에 있는 값이 범위 밖일 때 아무 액션하지 않기
    if right< index or index < left:
        return
    if left == right:
        tree[node] = [value, left]
        return
    mid = (left + right) //2
    update(node*2, left, mid, index, value)
    update(node*2+1, mid+1, right, index, value)

    smaller_node = node*2
    if tree[node*2][VALUE] > tree[node*2+1][VALUE]:
        smaller_node = node*2+1
    # 각 레벨에 따른 범위 중 최솟값으로 배치하기
    tree[node] = [tree[smaller_node][VALUE], tree[smaller_node][INDEX]]

for _ in range(query):
    order = list(map(int, input().split()))
    if order[0] == 1:
        # 1번째 노트부터 탐색, 1~seqLen만큼의 구간을, order[1]에 있는 값을 order[2]으로 변경
        update(1, 1, seqLen, order[1], order[2])
    else:
        print(tree[1][INDEX])