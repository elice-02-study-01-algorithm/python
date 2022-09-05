from itertools import combinations

n, m = map(int, input().split())

lst = [i + 1 for i in range(n)]

for i in combinations(lst, m):
    for j in i:
        print(j, end=" ")
    print()