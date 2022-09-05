# 시간복잡도와 공간복잡도 개선한 코드
# 기존의 슬라이싱 방법에서 왼쪽, 오른쪽 서브트리 끝의 좌표값 접근 형식으로 바꿈
from sys import stdin

def PostOrder(preL, preR, inL, inR): # ex) 전위순회 왼쪽 서브트리 끝의 좌표값 = 0, 중위순회 오른쪽 서브트리 끝의 좌표값 = n - 1
    if preL > preR or inL > inR:
        return
    root = preorder[preL]
    mid = pos[root]
    left = mid - inL # 왼쪽 서브트리 노드 개수
    right = inR - mid # 오른쪽 서브트리 노드 개수
    PostOrder(preL + 1, preL + left, inL, inL + left - 1) # 왼쪽 서브트리 탐색
    PostOrder(preR - right + 1, preR, inR - right + 1, inR) # 오른쪽 서브트리 탐색
    print(root, end = " ") # 후위이므로 탐색 끝나고 출력

input = stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().strip().split()))
    inorder = list(map(int, input().strip().split()))
    pos = [0 for _ in range(n + 1)] # [0] * (n + 1) 1번 노드부터 시작하므로 하나를 더 만들어 줌
    for i in range(n):
        pos[inorder[i]] = i # 각 노드번호 인덱스에 중위 순회의 인덱스 값을 넣어줌
    PostOrder(0, n - 1, 0, n - 1)
    print()