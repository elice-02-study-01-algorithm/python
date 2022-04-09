import sys

def postorder(preorder, inorder) :
  if len(preorder) == 0 :
    return
  elif len(preorder) == 1 :
    answer.append(preorder[0])
    # append 그 자체를 원소로 넣고 '[]'까지 포함, extend는 iterable 각 항목을 넣음 '[]' 포함 X
    # answer.extend(preorder)
    return

  # 루트는 전위순회의 0번째
  root = preorder[0]
  root_idx = inorder.index(root)

  # 왼쪽 부분 트리
  postorder(preorder[1:root_idx + 1], inorder[:root_idx])
  
  # 오른쪽 부분 트리
  postorder(preorder[root_idx + 1:], inorder[root_idx + 1:])
  
  # 왼쪽, 오른쪽 부분 트리를 다했다면 루트
  answer.append(root)

# 테스트 케이스 개수 T 입력
T = int(input())

for _ in range(T) :
  N = int(input())
  
  preorder = list(map(int, sys.stdin.readline().split()))
  inorder = list(map(int, sys.stdin.readline().split()))
  answer = []
  
  postorder(preorder, inorder)
  print(*answer)