from sys import stdin

num = int(stdin.readline().strip())
result = 0
arr = []
for _ in range(num):
    a,b = map(int,stdin.readline().strip().split())
    result += b
    arr.append(a)

arr.append(0)
arr = sorted(arr)

for i in range(1,num+1):
    result += i*arr[i]

print(result)