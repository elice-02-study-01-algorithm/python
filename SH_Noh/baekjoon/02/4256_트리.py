from sys import stdin

def PostOrder(preorder, inorder):
    if preorder:
        root = preorder[0] # 전위 순회의 첫 번째 값은 전체 트리의 루트노드
        mid = inorder.index(root) # 중위 순회에서는 루트를 기준으로 왼쪽이 서브트리/오른쪽 서브트리
        # 왼쪽, 오른쪽 서브트리의 순회 결과 출력
        PostOrder(preorder[1:mid+1], inorder[:mid])
        PostOrder(preorder[mid+1:], inorder[mid+1:])
        print(root, end = " ") # 후위이므로 탐색 끝나고 출력

input = stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().strip().split()))
    inorder = list(map(int, input().strip().split()))
    PostOrder(preorder, inorder)
    print()

# 출처 : https://8iggy.tistory.com/112 | https://kimmeh1.tistory.com/506