# 처음 배열의 크기는 0
# 새로운 배열의 크기는 원소의 수 이상인 2의 거듭제곱 중에서 가장 작은 값
# a는 최대 1000, b는 최대 10000
# 2의 거듭제곱 중 1000000000까지 가능...
from typing import List

def solution(queries: List[List[int]]) -> int:
    answer = 0
    # (현재 개수, 현재 배열 크기)
    arr_dict = [[0, 0] for _ in range(1001)]
    for arr, num in queries:
        if arr_dict[arr][0] + num <= arr_dict[arr][1]:
            arr_dict[arr][0] += num
        else:
            if arr_dict[arr][0] != 0:
                answer += arr_dict[arr][0]
            arr_dict[arr][0] += num # 현재 개수에 일단 더하고
            exponent = len(bin(arr_dict[arr][0])) - 2 # 크기 늘리기
            arr_dict[arr][1] = 2 ** exponent
    return answer