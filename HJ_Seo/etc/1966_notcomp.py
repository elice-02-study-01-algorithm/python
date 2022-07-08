from sys import stdin

n = int(stdin.readline().strip())

for i in range(n):
    leng, idx = map(int,stdin.readline().strip().split())
    arr = [int(a) for a in stdin.readline().strip().split()]
    
    maxi = max(arr)
    order = arr[idx]

    if maxi == order:
        print(idx+1)
        continue
    
    near_max_idx = -1
    result = 0
    
    for i in range(9,order,-1):
        if arr.count(i) != 0:
            near_max_idx = arr[idx:].index(i)
            # print(near_max_idx)
        result += arr.count(i)
    
    # print(arr.count(order),arr[idx+1:near_max_idx].count(order))
    result += arr.count(order) - arr[idx+1:near_max_idx].count(order)

    print(result)