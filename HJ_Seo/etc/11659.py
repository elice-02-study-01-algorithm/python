from sys import stdin
N,M = map(int,stdin.readline().strip().split())

nums = [0]+list(map(int,stdin.readline().strip().split()))
for i in range(N):
    nums[i+1] += nums[i]

for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    print(nums[b]-nums[a-1])
