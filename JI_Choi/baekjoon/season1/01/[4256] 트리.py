T = int(input())
treeList = [] # 각각의 케이스에 대해서, 모든 노드의 left, right 정보 저장
orderList = [] # 각각의 케이스에 대해서, preorder, inorder 정보 저장

for _ in range(T):
  n = int(input())
  tree = [[i, 0, 0] for i in range(1,n+1)]  # 모든 노드의 left, right 값을 0으로 초기 설정
  treeList.append(tree)
  order = [list(map(int, input().split())) for _ in range(2)]
  orderList.append(order)

# preorder, inorder로부터 모든 노드의 left, right 정보를 복원해서 treeList의 i번째 인덱스에 저장
# i번째 케이스를 다루는 함수 (단, i는 0부터 시작)
def getTree(preorder, inorder, i) :
  global treeList

  # 빈 배열인 경우, 함수 종료
  if len(preorder) == 0:
    return
  
  # preorder의 길이가 1인 경우, left, right의 정보는 0 (그대로 반환해주는 것과 값이 동일)
  elif len(preorder) == 1:
    return
  
  # preorder의 길이가 2인 경우
  elif len(preorder) == 2:
    root = preorder[0]
    # preorder과 inorder의 형태가 다르면(역순이면), right가 없음
    if inorder[0] != root:
        # treeList의 i번째 인덱스의 root-1번째 인덱스(root 노드)의 left값에 정보를 추가
        treeList[i][root-1][1] = preorder[1]
    else:
      # preorder과 inorder의 형태가 같으면, left가 없음
      # treeList의 i번째 인덱스의 root-1번째 인덱스의 right값에 정보를 추가
      treeList[i][root-1][2] = preorder[1]

  # preorder의 길이가 3이상인 경우
  else:
    # preorder의 첫 원소는 루트
    root = preorder[0]
    # inorder에서 root의 인덱스 위치 찾기
    rootIndex = inorder.index(root)

    # root의 index를 기준으로 새로운 preorder, inorder 생성 (각각 2개)
    # 빈 배열([])이 생성되는 경우도 존재 (이 경우, 재귀함수의 조건문에서 걸러짐)
    subPreorder = [preorder[1:rootIndex+1], preorder[rootIndex+1:]]
    subInorder = [inorder[:rootIndex], inorder[rootIndex+1:]]

    # 각각의 subPreorder의 첫 원소는 루트의 left, right
    leftNode = subPreorder[0][0] if subPreorder[0] != [] else 0
    rightNode = subPreorder[1][0] if subPreorder[1] != [] else 0

    # left, right 정보를 저장
    treeList[i][root-1][1] = leftNode
    treeList[i][root-1][2] = rightNode

    # subPreorder, subinorder에 대해 재귀함수 실행
    getTree(subPreorder[0], subInorder[0], i)
    getTree(subPreorder[1], subInorder[1], i)

    return

# postorder을 반환하는 함수
# 각각의 노드에 대한 left, right 정보가 기록된 배열과 root의 인덱스를 입력
def postorder(tree, rIndex):
  result = []

  if tree[rIndex][1] != 0:
    leftIndex = tree[rIndex][1] - 1
    result = result + postorder(tree, leftIndex)
  
  if tree[rIndex][2] != 0:
    rightIndex = tree[rIndex][2] - 1
    result = result + postorder(tree, rightIndex)
  
  result.append(tree[rIndex][0])

  return result

## 각 케이스마다 preorder 결과를 출력 ##
for i in range(T):
  preorder = orderList[i][0]
  inorder = orderList[i][1]
  getTree(preorder, inorder, i)

  tree = treeList[i]
  rIndex = preorder[0] - 1
  postorderInfo = postorder(tree, rIndex)

  print(' '.join(str(v) for v in postorderInfo))