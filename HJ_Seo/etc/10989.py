from sys import stdin

n = int(stdin.readline().strip())

nums = [0]*10001

for i in range(n):
    nums[int(stdin.readline().strip())] += 1

for j in range(1,10001):
    if nums[j] != 0:
        for k in range(nums[j]):
            print(j) 

