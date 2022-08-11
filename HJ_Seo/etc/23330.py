# https://www.acmicpc.net/problem/23330

from sys import stdin

n = int(stdin.readline().strip())
nums = sorted(map(int,stdin.readline().strip().split()),reverse=True)

num = 0

for i in range(n):
    num += 2*(n-1-2*i)*nums[i]

print(num)

# print(5*8+4*4-2*4-8)

'''
1,2,3,4,5..

5.. +9 -1
4.. +7 -3
3.. +5 -5
2.. +3 -7
1.. +1 -9 
'''
