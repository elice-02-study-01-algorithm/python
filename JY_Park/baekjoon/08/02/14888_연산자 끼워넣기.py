n = int(input())
sequence = list(map(int, input().split()))
op = list(map(int, input().split()))

max_num = -1000000001
min_num = 1000000001

# dfs: 가능한 모든 경로(후보)를 탐색한다.
# 백트래킹: 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더이상 가지 않고 되돌아간다.
# 주로 문제 풀이에서는 DFS 등으로 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대로 될 수 없는 상황을 정의하고, 그러한 상황일 경우에는 탐색을 중지시킨 뒤 그 이전으로 돌아가서 다시 다른 경우를 탐색하게끔 구현

def dfs_back(idx, result, p, m, mul, div):
    global min_num, max_num

    # 백트래킹은 
    if idx == n:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    # 숫자를 문자로 받아서 해당 값을 사용할 때 -1 해줌.
    if p:
        dfs_back(idx + 1, result + sequence[idx], p - 1, m, mul, div)
    if m:
        dfs_back(idx + 1, result - sequence[idx], p, m - 1, mul, div)
    if mul:
        dfs_back(idx + 1, result * sequence[idx], p, m, mul - 1, div)
    # 정수 나눗셈으로 몫만
    if div:
        dfs_back(idx + 1, int(result / sequence[idx]), p, m, mul, div - 1)

dfs_back(1, sequence[0], op[0], op[1], op[2], op[3])

print(max_num)
print(min_num)