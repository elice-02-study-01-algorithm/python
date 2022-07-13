from sys import stdin

n = int(stdin.readline().strip())
lst = list(map(int,stdin.readline().strip().split()))

check_lst1 = [1 for _ in range(n)]
check_lst2 = [1 for _ in range(n)]

for i in range(1,n):
    if lst[i] > lst[i-1]:
        check_lst1[i] = check_lst1[i-1] + 1
    elif lst[i] < lst[i-1]:
        check_lst2[i] = check_lst2[i-1] + 1
    else:
        check_lst1[i] = check_lst1[i-1] + 1
        check_lst2[i] = check_lst2[i-1] + 1

print(max(check_lst1 + check_lst2))