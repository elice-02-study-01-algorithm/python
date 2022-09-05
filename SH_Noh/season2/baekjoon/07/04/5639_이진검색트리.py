import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

tree = []
while True:
    try:
        num = int(input())
    except:
        break
    tree.append(num)

def postorder(start, end):
    # 시작이 끝보다 크면 리턴
    if start > end:
        return
    mid = end + 1
    # 서브 트리 찾기
    for i in range(start + 1, end + 1):
        # 루트보다 크면 오른쪽 서브 트리
        if tree[start] < tree[i]:
            mid = i
            break
    
    postorder(start + 1, mid - 1) # 왼쪽 서브 트리
    postorder(mid, end) # 오른쪽 서브 트리
    print(tree[start])

postorder(0, len(tree) - 1)
