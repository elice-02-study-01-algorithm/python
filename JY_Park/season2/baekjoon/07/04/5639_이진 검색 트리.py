# sys.setrecursionlimit(10000) 를 입력하지 않으면 런타임 오류가 발생한다.
# 파이썬의 기본 재귀 한도는 1000이고, 재귀 깊이가 1000을 넘어갈 경우 모듈을 추가해야 한다.

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

tree = []
while True:
    try:
        node = int(input())
        tree.append(node)
    except:
        break

# 후위 순회 // (왼쪽 자식) (오른쪽 자식) (루트)
def post_order(start, end):
    # 재귀 종료 조건
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            mid = i
            break

    # 왼쪽 트리
    post_order(start + 1, mid - 1) 
    # 오른쪽 트리
    post_order(mid, end)
    # 루트 노드 출력
    print(tree[start])

post_order(0, len(tree) - 1)