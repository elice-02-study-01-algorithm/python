from sys import stdin

n = int(input())
nums = list(map(int,stdin.readline().strip().split()))

maxnum = max(nums)

print(sum(nums)/(n*maxnum)*100)