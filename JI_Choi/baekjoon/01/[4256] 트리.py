T = int(input())
treeList = []   # left, right 정보 저장
orderList = []  # preorder, inorder 정보 저장

for _ in range(T):
  n = int(input())
  tree = [[i,0,0] for i in range(1,n+1)]
  treeList.append(tree)
  order = [list(map(int, input().split())) for _ in range(2)]
  orderList.append(order)

## Tree 구하는 함수 ##
def getTree(preorder, inorder, i):
  global treeList

  # preorder, inorder => subPreorder, subInorder를 만드는 과정에서 빈 배열이 생길 가능성이 존재
  if len(preorder) == 0:
    return
  
  # 자식 노드가 없는 경우
  elif len(preorder) == 1:
    return
  
  # 루트에 자식 노드가 존재하는 경우
  elif len(preorder) == 2:
    root = preorder[0]
    if inorder[0] != root:
      # left에 추가
      treeList[i][root-1][1] = preorder[1]
    else:
      # right에 추가
      treeList[i][root-1][2] = preorder[1]

  # 전위 순회의 첫 원소는 루트
  root = preorder[0]
  # 중위 순회에서 루트의 인덱스 위치
  rIdx = inorder.index(root)

  subPreorder = [preorder[1:rIdx+1], preorder[rIdx+1:]]
  subInorder = [inorder[:rIdx], inorder[rIdx+1:]]

  left = subPreorder[0][0] if subPreorder[0] !=[] else 0
  right = subPreorder[1][0] if subPreorder[1] !=[] else 0

  # 루트의 left, right 정보를 기록
  treeList[i][root-1][1] = left
  treeList[i][root-1][2] = right

  getTree(subPreorder[0], subInorder[0], i)
  getTree(subPreorder[1], subInorder[1], i)

  return

## tree 정보, root의 index를 입력 => 후위 순회 배열 반환 ##
def postorder(tree, index) :

    result = []
    
    if tree[index][1] != 0:
        leftIndex = tree[index][1] - 1
        result = result + postorder(tree, leftIndex)
    
    if tree[index][2] != 0:
        rightIndex = tree[index][2] - 1
        result = result + postorder(tree, rightIndex)
        
    result.append(tree[index][0])

    return result

## 각 테스트 케이스마다 후위 순회한 결과 출력 ##
for i in range(T):
  Preorder = orderList[i][0]
  Inorder = orderList[i][1]
  getTree(Preorder, Inorder, i)
  Tree = treeList[i]
  rIndex = orderList[i][0][0] - 1   # root 숫자 = 저장된 위치의 인덱스 + 1
  tlist = postorder(Tree, rIndex)   # 후위 순회 배열
  values = ' '.join(str(v) for v in tlist)

  print(values)