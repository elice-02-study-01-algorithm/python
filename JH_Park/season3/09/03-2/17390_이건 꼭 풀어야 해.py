import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

order_list = sorted(arr)

for i in range(1, n):
    order_list[i] = order_list[i- 1] + order_list[i]

order_list = [0] + order_list
    
for _ in range(q):
    l, r = map(int, input().split())
    print(order_list[r] - order_list[l-1])