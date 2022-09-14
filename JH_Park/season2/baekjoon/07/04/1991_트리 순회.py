class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preOrder(node):
    if node is None:
        return
    print(node.val, end="")
    preOrder(node.left)
    preOrder(node.right)
    
def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.val, end="")
    inOrder(node.right)
    
def postOrder(node):
    if node is None:
        return
    postOrder(node.left)    
    postOrder(node.right)
    print(node.val, end="")

n = int(input())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
node_arr = []
for i in range(n):
    node_arr.append(TreeNode(alphabet[i]))
for i in range(n):
    root, l, r = list(input().split(' '))
    if l != ".":
        node_arr[ord(root) % 65].left = node_arr[ord(l) % 65]
    if r != ".":
        node_arr[ord(root) % 65].right = node_arr[ord(r) % 65]

preOrder(node_arr[0])
print()
inOrder(node_arr[0])
print()
postOrder(node_arr[0])