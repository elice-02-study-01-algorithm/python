from sys import stdin
input = stdin.readline

class Node:
  def __init__(self,data,left_node,right_node):
      self.data = data
      self.left_node = left_node
      self.right_node = right_node

# 전위 순회, ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
def pre_order(node):
  print(node.data,end='')
  if node.left_node != None:
    pre_order(tree[node.left_node])
  if node.right_node != None:
    pre_order(tree[node.right_node])

# 중위 순회, DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
def in_order(node):
  if node.left_node != None:
    in_order(tree[node.left_node])
  print(node.data,end='')
  if node.right_node != None:
    in_order(tree[node.right_node])

# 후위 순회, DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
def post_order(node):
  if node.left_node != None:
    post_order(tree[node.left_node])
  if node.right_node != None:
    post_order(tree[node.right_node])
  print(node.data,end='')


n = int(input())
tree = {}

for i in range(n):
  data, left_node, right_node = input().split()
  if left_node == '.':
    left_node = None
  if right_node == '.':
    right_node = None
  tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])