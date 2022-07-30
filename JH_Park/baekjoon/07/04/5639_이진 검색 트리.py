import sys
sys.setrecursionlimit(10**6)

def postorder(start, end):
    if start > end: return
    root = pre_order[start]
    idx = start + 1
    
    for i in range(idx, end + 1):
        if pre_order[i] > root:
            idx = i
            break
    # 왼쪽 오른쪽 반갈라치기
    postorder(start + 1, idx -1)
    postorder(idx, end)
    print(root)
    
pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

postorder(0, len(pre_order) - 1)