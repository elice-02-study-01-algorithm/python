'''
node별로 left, right 할당해줘야하기 때문에 class로 구현하는 데에 집착했다.
그런데 class 구현이 까다롭기도 하고, 익숙치 않은 게 커서 결국엔 dictionary로 풀게 됐다.
30840 KB 72 ms
'''

N = int(input())
# A는 어떤 경우에라도 있으니 미리 세팅하기
_, aLeft, aRight = input().split()
treeDic = {'A':(aLeft, aRight)}

for _ in range(N-1):
    node, nodeLeft, nodeRight = input().split()
    treeDic[node] = (nodeLeft, nodeRight)

# {'A': ('B', 'C'), 'B': ('D', '.'), 'C': ('E', 'F'), 'E': ('.', '.'), 'F': ('.', 'G'), 'D': ('.', '.'), 'G': ('.', '.')}

# 전위순회
def preOrder(start):
    result = ''
    node = start
    if start == '.':
        return ''
    if treeDic[node]:
        result += node
        result += preOrder(treeDic[node][0])
        result += preOrder(treeDic[node][1])
    return result

# 중위순회
def inOrder(start):
    result = ''
    node = start
    if node == '.':
        return ''
    if treeDic[node]:
        result += inOrder(treeDic[node][0])
        result += node
        result += inOrder(treeDic[node][1])
    return result

# 후위순회
def postOrder(start):
    result = ''
    node = start
    if node == '.':
        return ''
    if treeDic[node]:
        result += postOrder(treeDic[node][0])
        result += postOrder(treeDic[node][1])
        result += node
    return result

print(preOrder('A'))
print(inOrder('A'))
print(postOrder('A'))