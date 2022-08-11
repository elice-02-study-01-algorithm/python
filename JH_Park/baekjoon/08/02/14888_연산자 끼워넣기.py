from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
operator = ['+'] * plus
operator += ['-'] * minus
operator += ['x'] * multi
operator += ['/'] * div
operator = list(set(permutations(operator, len(operator))))

result = []
for oper in operator:
    num = nums[0]
    for i in range(1, len(nums)):
        if oper[i-1] == '+':
            num += nums[i]
        elif oper[i-1] == '-':
            num -= nums[i]
        elif oper[i-1] == 'x':
            num *= nums[i]
        else:
            if num < 0 < nums[i]:
                num = -(-num // nums[i])
            else:
                num = num // nums[i]
    result.append(num)
print(max(result))
print(min(result))