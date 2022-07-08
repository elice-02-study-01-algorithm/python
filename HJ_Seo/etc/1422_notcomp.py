from sys import stdin

K,N = map(int,stdin.readline().strip().split())

nums = []

for _ in range(K):
    nums.append(stdin.readline().strip())

nums = sorted(nums, key = lambda x: (len(x),-int(x)))
maxnum = str(max(map(int,nums)))

result = ''
temp = ''
choose = 1 if len(nums[0]) == len(nums[-1]) else 0

for i in range(N):
    if i<K:
        result += nums[i]
    else:
        if choose == 1:  #모든 숫자의 크기가 10^n 상에서 동일하기 때문에 앞에 있는 가장 큰 숫자를 더해주는 것이 좋음.
            temp += nums[0]
        else:
            result += maxnum #최소 한 숫자가 10^n 상에서 크기가 다름.. 끝에 넣어서 더해주는 것이 좋다.

result = temp + result

print(result)

'''
4 4
79
72
70
7
WANTED: 7977270
'''