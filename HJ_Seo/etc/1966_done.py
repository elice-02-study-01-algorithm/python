# from sys import stdin

# n = int(stdin.readline().strip())

# for i in range(n):
#     leng, idx = map(int,stdin.readline().strip().split())
#     arr = [int(a) for a in stdin.readline().strip().split()]
    
#     maxi = max(arr)
#     order = arr[idx]

#     if maxi == order:
#         print(idx+1)
#         continue
    
#     near_max_idx = -1
#     result = 0
    
#     for i in range(9,order,-1):
#         if arr.count(i) != 0:
#             near_max_idx = arr[idx:].index(i)
#             # print(near_max_idx)
#         result += arr.count(i)
    
#     # print(arr.count(order),arr[idx+1:near_max_idx].count(order))
#     result += arr.count(order) - arr[idx+1:near_max_idx].count(order)

#     print(result)

# ! 뭐땜시 틀렸는지 기억 안남..

from sys import stdin

cases = int(stdin.readline().strip())
# lst = []
for _ in range(cases):
    N,M = map(int,stdin.readline().strip().split())
    docu = tuple(map(int,stdin.readline().strip().split()))
    target = sorted({i for i in set(docu) if i>=docu[M]},reverse=True)
    # print('target =',target)
    orders = [None]*N
    order = 1
    last = 0
    tmp = 0
    
    for i in target:
        for j in range(last,N):
            if docu[j] == i:
                orders[j] = order
                order += 1
                tmp = j
                # print(orders)
                
        for j in range(0,last):
            if docu[j] == i:
                orders[j] = order
                order += 1
                tmp = j
                # print(orders)

        last = tmp
    
    print(orders[M])
#     lst.append(orders[M])

# lst2 = []
# while True:
#     try:
#         lst2.append(int(input()))
#     except:
#         break

# lst3 = []
# for i in range(100):
#     if lst[i] != lst2[i]:
#         lst3.append(i)

# print(lst)
# print(lst2)
# print(lst3)
        

'''

4
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
9 3
4 3 2 2 3 5 2 1 3

output(차례대로) : 1, 2, 5, 7
'''
                    
    