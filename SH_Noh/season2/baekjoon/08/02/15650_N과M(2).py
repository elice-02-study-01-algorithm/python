# from itertools import combinations
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
N_list = [x for x in range(1, N + 1)]
# combi = list(combinations(N_list, M))
# for i in range(len(combi)):
#     print(*combi[i])

# 백트래킹 시도
combi = [0] * M
isused = [False] * (N + 1)

def backtracking(num, idx):
    if idx == M:
        # if sorted(combi) == combi:
        print(*combi)
        return

    for i in range(num, N + 1):
        if not isused[i]:
            combi[idx] = i
            isused[i] = True
            backtracking(i + 1, idx + 1)
            isused[i] = False

if __name__ == "__main__":
    backtracking(1, 0)