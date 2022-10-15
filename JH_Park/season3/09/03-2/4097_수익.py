import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0:
        break
    
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    for i in range(1, n):
        if arr[i-1] + arr[i] > arr[i]:
            arr[i] = arr[i-1] + arr[i]
    print(max(arr))