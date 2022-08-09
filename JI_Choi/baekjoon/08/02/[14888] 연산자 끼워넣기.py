import sys
input = sys.stdin.readline

# 수의 개수 입력받기
n = int(input())
# 숫자들 입력 받기
data = list(map(int, input().split()))
# 연산자의 개수 입력 받기
add, sub, mul, div = map(int, input().split())

# 최대값과 최솟값 선언
max_value = -1e9
min_value = 1e9

# dfs 매서드 정의
def dfs(i, acc):
    global add, sub, mul, div, max_value, min_value
    # i == n인 경우
    if i == n:
        max_value = max(max_value, acc)
        min_value = min(min_value, acc)
    # i < n인 경우
    else:
        # add
        if add > 0:
            add -= 1
            dfs(i+1, acc + data[i])
            add += 1
        # sub
        if sub > 0:
            sub -= 1
            dfs(i+1, acc - data[i])
            sub += 1
        # mul
        if mul > 0:
            mul -= 1
            dfs(i+1, acc * data[i])
            mul += 1
        # div
        if div > 0:
            div -= 1
            dfs(i+1, int(acc / data[i]))
            div += 1

# dfs 시행
dfs(1, data[0])

print(max_value)
print(min_value)

# 2
# 5 6
# 0 0 1 0

# dfs(1, 5)
# dfs(2, 30) -> max_value = 30, min_value = 30
# 30
# 30

# 3
# 3 4 5
# 1 0 1 0

# dfs(1, 3)
# dfs(2, 7) -> dfs(3, 35) -> max_value = 35, min_value = 35
# dfs(2, 12) -> dfs(3, 17) -> min_value = 17
# 35
# 17