import sys
input = sys.stdin.readline

# 수열의 크기 입력받기
n = int(input())
# 수열 입력받기 (인덱스 조정을 위해 " [0] + " 을 추가)
arr = [0] + list(map(int, input().strip().split()))
# 트리 선언 (크기를 3*n으로 지정하는 것에 대한 이해가 더 필요)
tree = [[0, 0]] * (3*n)  # 첫 원소는 value 값, 두번째 원소는 index 값

# 수열을 세그먼트 트리로 변환하는 함수
def init(node, start, end):
    # start와 end가 같은 경우
    if (start == end):
        # tree[node]에 값 할당
        tree[node] = [arr[start], start]
    # start와 end가 다른 경우
    else:
        # mid 정의
        mid = (start + end) // 2
        # 절반에 대해 각각 재귀적 실행
        init(node*2, start, mid)
        init(node*2 + 1, mid + 1, end)

        # smaller_node 정의
        smaller_node = node*2
        if tree[node*2][0] > tree[node*2 + 1][0]:
            smaller_node = node*2 + 1
    
        # tree[부모 노드]에 값 할당 (단, smaller_node의 부모 노드를 의미)
        tree[node] = [tree[smaller_node][0], tree[smaller_node][1]]

# 수열을 세그먼트 트리로 변환
init(1, 1, n)

# 쿼리의 개수 입력받기
m = int(input())

# 세그먼트 트리를 최신화하는 함수
def update(node, left, right, index, value):
    # 범위를 벗어난 경우
    if right < index or index < left:
        return

    # left와 right가 같은 경우
    if left == right:
        # tree[node] 최신화
        tree[node] = [value, left]
        return

    # mid 정의
    mid = (left + right) // 2
    # 절반에 대해 각각 재귀적 실행
    update(node*2, left, mid, index, value)
    update(node*2 + 1, mid + 1, right, index, value)

    # smaller_node 정의
    smaller_node = node*2
    if tree[node*2][0] > tree[node*2 + 1][0]:
        smaller_node = node*2 + 1
    
    # tree[부모 노드] 값 최신화 (단, smaller_node의 부모 노드를 의미)
    tree[node] = [tree[smaller_node][0], tree[smaller_node][1]]

# 쿼리의 개수만큼 반복
for _ in range(m):
    # 쿼리 배열 형태로 입력받기
    info = list(map(int, input().split()))
    # 쿼리의 내용이 '1 i v'인 경우
    if info[0] == 1:
        update(1, 1, n, info[1], info[2])
    # 쿼리의 내용이 '2'인 경우
    else:
        print(tree[1][1])