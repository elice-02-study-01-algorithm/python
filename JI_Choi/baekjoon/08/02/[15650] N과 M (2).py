from itertools import combinations
from sys import stdin
input = stdin.readline

# N, M 입력받기
n, m = map(int, input().split())

# n이하의 자연수로 이루어진 배열 생성
arr = [i for i in range(1, n+1)]

# 모든 경우의 수 구하기
combination_list = list(combinations(arr, m))

# 각 수열을 공백으로 구분해서 출력
for i in combination_list:
    print(*i)