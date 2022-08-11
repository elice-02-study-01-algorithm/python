# python3로 통과
# 백트래킹 사용
from sys import stdin
input = stdin.readline

def backtracking(sum, idx, add, sub, mul, div):
    global maximum, minimum
    if idx == N:
        maximum = max(maximum, sum)
        minimum = min(minimum, sum)
        return

    if add > 0:
        backtracking(sum + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        backtracking(sum - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        backtracking(sum * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        backtracking(int(sum / nums[idx]), idx + 1, add, sub, mul, div - 1)

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    maximum = -1e9
    minimum = 1e9

    backtracking(nums[0], 1, add, sub, mul, div)
    print(maximum)
    print(minimum)