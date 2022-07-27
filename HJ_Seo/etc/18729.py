# https://www.acmicpc.net/problem/18729

from sys import stdin

case = int(input())

for _ in range(case):
    n,k = map(int,stdin.readline().strip().split())
    nums = sorted(list(map(int,stdin.readline().strip().split())))
    
    if k == 0:
        print(sum(nums))
    else:
        print(max(sum(nums[:n-k]),nums[-1]))