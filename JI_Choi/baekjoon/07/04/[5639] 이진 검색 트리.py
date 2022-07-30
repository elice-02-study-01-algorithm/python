import sys
sys.setrecursionlimit(100000)
info = []

# 개수가 정해지지 않은 경우 입력값 받기
while True:
    try:
        num = int(sys.stdin.readline())
        # 배열에 입력값 추가
        info.append(num)
    except:
        break

# 후위 순회
def postorder(arr):
    # 트리를 전위 순회한 결과값 배열에 대한 길이
    d = len(arr)
    # 길이가 1인 경우
    if d <= 1:
        return arr
    # 길이가 1보다 큰 경우
    for i in range(1, d):
        # i번째 원소가 루트보다 큰 경우
        if arr[i] > arr[0]:
            # 후위 순회는 (왼쪽 - 오른쪽 - 루트) 형태
            return postorder(arr[1:i]) + postorder(arr[i:]) + [arr[0]]
    # 모든 원소들이 루트보다 작은 경우
    return postorder(arr[1:]) + [arr[0]]

# 후위 순회에 대한 원소를 하나씩 출력
for i in postorder(info):
    print(i)
