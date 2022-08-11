from sys import stdin

# 수열의 크기 입력받기
n = int(stdin.readline())
# 수열 입력받기
arr = list(map(int, stdin.readline().strip().split()))
# 쿼리의 개수 입력받기
m = int(stdin.readline())

for _ in range(m):
    #쿼리 입력받기
    info = list(map(int, stdin.readline().strip().split()))

    # 쿼리의 내용이 '1 i v'인 경우
    if info[0] == 1:
        # 수열의 i번째 성분을 v로 교체
        arr[int(info[1]) - 1] = int(info[2])

    # 쿼리의 내용이 '2'인 경우
    else:
        # 가장 작은 원소 찾기
        min_value = min(arr)
        # 값이 min_value인 성분 중 가장 작은 인덱스 값 찾기
        min_index = arr.index(min_value)
        # 인덱스 출력 (문제에서는 첫 인덱스가 1)
        print(min_index + 1)
