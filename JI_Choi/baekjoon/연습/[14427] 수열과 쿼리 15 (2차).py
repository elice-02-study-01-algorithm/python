from sys import stdin

# 수열의 크기 입력받기
n = int(stdin.readline())
# 수열 입력받기
arr = list(map(int, stdin.readline().strip().split()))
# 쿼리의 개수 입력받기
m = int(stdin.readline())

min_value = min(arr)
min_index = arr.index(min_value)

for _ in range(m):
    #쿼리 입력받기
    info = stdin.readline().strip()

    # 쿼리의 내용이 '1 i v'인 경우
    if info[0] == '1':
        # i-1번째 인덱스가 min_index가 아닌 경우
        if int(info[2]) - 1 != min_index:
            # i-1번째 성분이 min_value보다 작은 경우
            if int(info[4]) < min_value:
                # min_index, min_value 최신화
                min_index = int(info[2]) - 1
                min_value = int(info[4])
            # i-1번째 성분이 min_value와 같은 경우
            if int(info[4]) == min_value:
                # i-1번째 인덱스가 min_index보다 작은 경우
                if int(info[2]) - 1 < min_index:
                    # min_index 최신화
                    min_index = int(info[2]) - 1
            
        # i-1번째 인덱스가 min_index인 경우
        if int(info[2]) - 1 == min_index:
            # i-1번째 성분이 min_value보다 작은 경우
            if int(info[4]) < min_value:
                min_value = int(info[4])
            # i-1번째 성분이 min_value보다 큰 경우
            if int(info[4]) > min_value:
                min_value = min(arr)
                min_index = arr.index(min_value)

        # 수열의 i번째 성분을 v로 교체
        arr[int(info[2]) - 1] = int(info[4])


    # 쿼리의 내용이 '2'인 경우
    else:
        # 인덱스 출력 (문제에서는 첫 인덱스가 1)
        print(min_index + 1)
