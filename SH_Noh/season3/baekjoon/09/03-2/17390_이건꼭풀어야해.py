from sys import stdin
input = stdin.readline

N, Q = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
# for i in range(Q):
#     L, R = map(int, input().split())
#     print(sum(array[L-1:R]))
    
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[i] + array[i])
 
for _ in range(Q):
    L, R = map(int,input().split())
    print(prefix_sum[R] - prefix_sum[L-1])